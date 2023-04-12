"""
Status Sentry - website uptime monitoring tool for casual users

Problem:

Solution:

Implementation:

Usage:

"""

import requests

from bs4 import BeautifulSoup

import re

import datetime

from decouple import config

import whois

import time

from pushbullet import Pushbullet

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

pb = Pushbullet(config('pb_api'))

push = True

class test():

    def __init__(self, url, name_servers):

        self.url = url
        self.name_servers = name_servers

        self.pass_count=0
        self.fail_count=0
        self.total=lambda fail_c, pass_c: fail_c+pass_c

        self.report = ""

    def echo(self, status, output):
        if status is True:
            print(f"\033[32m\u2714 {output} \033[0m")
            self.pass_count+=1
        if status is False:
            print(f"\033[91m\u2717 {output} \033[0m")
            self.report += str(output)+"\n"
            self.fail_count+=1
        

    def find_contacts(self):
        print("Checking contact details @ "+self.url)
        status = True
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all phone numbers on the page
        phone_pattern = re.compile(r'\b\d{4}[-.]?\d{3}[-.]?\d{4}\b')
        phone_numbers = []
        for match in phone_pattern.findall(soup.get_text()):
            phone_numbers.append(match)
        
        # Find all email addresses on the page
        email_pattern = re.compile(r'\b[\w.-]+@[\w.-]+\.\w{2,}\b')
        email_addresses = []
        for match in email_pattern.findall(soup.get_text()):
            email_addresses.append(match)
    
        errors= []
        correct_number="07761544030"
        if phone_numbers:
            [errors.append(number) for number in phone_numbers if number != correct_number]
        else:
            errors.append("No phone numbers found")
        
        correct_email="jb.enquiries@proton.me"
        if email_addresses:
            [errors.append(email) for email in email_addresses if email != correct_email]
        else:
            errors.append("No email addresses found")
        
        if errors:
            status = False
        else:
            errors=["Contact details correct"]

        self.echo(status,errors)
        return status, errors

    def send_report(self, report):
        push = pb.push_note(self.url+" Alert", report)    

    def read_status(self):
        """
        Reads the uptime file of a website
        """
        status = False
        output=self.url+" domain is inactive"
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
            
        if soup.find(id='ActiveDomain'):
            status = True
            output=self.url_+" domain is active"
        
        # If no keywords are found, assume it's not a parked domain
        self.echo(status, output)
        return status, output
    
    def check_website(self):
        print("Checking @ "+self.url+" is online")
        """
        Checks the webpage loads
        """
        status = False
        try:
            start_time = time.time()
            response = requests.get(self.url, verify = False)
            end_time = time.time()

            # Calculate the load time in seconds
            load_time = end_time - start_time

            # Print the load time in seconds
            print("Load time for", self.url, ":", load_time, "seconds")

            response.raise_for_status()
            output = self.url+" is up and running with status code "+str(response.status_code)
            status = True
        except requests.HTTPError as http_error:
            output = self.url+" is offline with HTTP error: "+str(http_error)
        except requests.ConnectionError as connection_error:
            output = self.url+" is offline with connection error:  "+str(connection_error)
        except requests.Timeout as timeout_error:
            output = self.url+" is offline with timeout error:  "+str(timeout_error)
        except requests.RequestException as request_exception:
            output = self.url+" is offline with unknown exception:  "+str(request_exception)

        return status, output

    def check_links(self):
        print("Checking links @ "+self.url)
        # Get the website's HTML content
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all links on the page
        links = soup.find_all("a")

        # Loop through each link and check if it loads without error
        for link in links:

            href = link.get("href")
            if href:
                if href.startswith("http"):
                    try:
                        link_response = requests.get(href)
                        status_code = link_response.status_code
                        # link_response.raise_for_status()
                        if status_code == 200:
                            self.echo(True, "Link "+href+" is working.")
                        elif status_code == 403:
                            self.echo(False, "403 Forbidden error for "+href+" "+str(link))
                        else:
                            self.echo(False, "Unexpected status code "+str(status_code)+" for "+href+" "+str(link))
                    except requests.exceptions.HTTPError:
                        self.echo(False, "Link "+href+" is broken. ")
        
        print("Checking script links @ "+self.url)
        script_urls=[]
        for script in soup.find_all('script'):
            script_text = script.string
            if script_text:
                pattern = re.compile(r'(?P<url>https?://[^\s<>"]+|www\.[^\s<>"]+)')
                script_urls = re.findall(pattern, script_text)
                # print(script_urls)

            if script_urls:
                for href in script_urls:
                    # print(href)
                    try:
                        link_response = requests.get(href)
                        try:
                            status_code = link_response.status_code
                            # link_response.raise_for_status()
                            if status_code == 200:
                                self.echo(True, "Link "+href+" is working.")
                            elif status_code == 403:
                                self.echo(False, "403 Forbidden error for "+href)
                            else:
                                self.echo(False, "Unexpected status code "+str(status_code)+" for "+href)
                        except requests.exceptions.HTTPError:
                            self.echo(False, "Link "+href+" is broken. ")
                    except:
                        pass


    def check_domain(self):
        # Get WHOIS information for the domain
        w = whois.query(self.url)

        # Get the expiration date of the domain
        expiration_date = w.expiration_date
        nameServers = w.name_servers

        for x in ["expire","expiration"]:
            for y in nameServers:
                print(y)
                if x in y:
                    self.echo(False, "The domain "+self.url+" has already expired!")
                    return
        
        for x in self.name_servers:
            for y in nameServers:
                print(y)
                if x in y:
                    self.echo(True, "The domain "+self.url+" is using nameserver "+y)
                    return    
            self.echo(False, "The domain "+self.url+" has an incorrect nameserver "+y)

        # Calculate the number of days until the domain expires
        days_until_expiration = (expiration_date - datetime.datetime.now()).days

        # Check if the domain is expired or expiring soon
        if days_until_expiration < 0:
            self.echo(False, "The domain "+self.url+" has already expired!")
        elif days_until_expiration < 60:
            self.echo(False, "The domain "+self.url+" is expiring soon! It will expire in "+str(days_until_expiration)+" days.")
        else:
            self.echo(True, "The domain "+self.url+" is not expiring soon. It will expire in "+str(days_until_expiration)+" days.")



if __name__ == "__main__":

    urls = [["http://www.boejaker.com",["abbey.ns.cloudflare.com","brad.ns.cloudflare.com"]],["http://www.maxhodl.com",["ns1.dns-parking.com","ns2.dns-parking.com"]],["http://boejaker.github.io",[]]]

    print(f"Testing {len(urls)} urls, {urls}")
    
    for u, name_servers in urls:
        # print(u,name_servers)
        t=test(u, name_servers)

        print(f"Analyzing website {u}")

        t.check_website()
        t.read_status()
        t.check_domain()
        t.check_links()
        t.find_contacts()

        if t.report and push:
            t.send_report(t.report)
        else:
            t.send_report("Operational")

        total=t.total(t.fail_count, t.pass_count)
        print(f"pass {t.pass_count}/{total} failed{t.fail_count}/{total}")


