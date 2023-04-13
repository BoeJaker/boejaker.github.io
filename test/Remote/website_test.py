"""
Status Sentry - website uptime monitoring tool for casual users

Problem:

Solution:

Implementation:

Usage:

"""

import requests
from requests.exceptions import SSLError

import re

import inspect

import time

import datetime

from decouple import config

import whois

from pushbullet import Pushbullet

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

pb = Pushbullet(config('pb_api')) # Import API key from .env file using decouple.

push = True # A switch that turns on/off pushing notifications, mainly for debugging.

class test():

    def __init__(self, url, name_servers, email, phone_numbers):

        self.url = url # This is the URL that the test is being run on
        self.name_servers = name_servers # The expected nameservers
        self.emails = emails
        self.phone_numbers = phone_numbers
        
        # Test counters
        self.pass_count = 0
        self.fail_count = 0
        self.total=lambda: self.pass_count+self.fail_count

        self.load_time = {} # An array of all the load times associated with this url - indexed by the url

        self.errors ="" #
        self.report = "" #

    def echo(self, status, output):
        if status is True:
            print(f"\033[32m\u2714 {output} \033[0m")
            self.pass_count+=1
        if status is False:
            print(f"\033[91m\u2717 {output} \033[0m")
            self.report += str(output)+"\n"
            self.fail_count+=1

    def process_status_code(self, url, status_code):
        if status_code == 200:
            # self.echo(True, "Link "+url+" is working. Status Code "+str(status_code))
            pass
        elif status_code == 403:
            self.echo(False, "403 Forbidden error for "+url)
        else:
            self.echo(False, "Unexpected status code "+str(status_code)+" for "+url)
    
    def request_handler(self, url):
        self.errors=""
        status = False # Start in an "error" state to catch everything unhandled
        try:
            # print(inspect.stack()[1][3])
            start_time = time.time()
            response = requests.get(url)
            end_time = time.time()

            # Calculate the load time in seconds
            self.load_time[url] = end_time - start_time

            response.raise_for_status()
            self.errors = url+" is up and running with status code "+str(response.status_code)
            status = True
        
        except SSLError as ssl_error:
            self.errors = url+" has an SSL certificate Error:  "+str(ssl_error)
        except requests.HTTPError as http_error:
            self.errors = url+" is offline with HTTP error: "+str(http_error)
        except requests.ConnectionError as connection_error:
            self.errors = url+" is offline with connection error:  "+str(connection_error)
        except requests.Timeout as timeout_error:
            self.errors = url+" is offline with timeout error:  "+str(timeout_error)
        except requests.RequestException as request_exception:
            self.errors = url+" is offline with unknown exception:  "+str(request_exception)
        except Exception as error:
             self.errors = url+" has an Unknown Error:  "+str(error)

        if self.errors:
            self.echo(status, self.errors)

        try:
            return(response, response.status_code, status)    
        except:
            return("Unknown error"+url, 0, False)    


    def find_contacts(self):
        print("Checking contact details @ "+self.url)
        response, status_code, status = self.request_handler(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        errors= []
        if self.phone_numbers:
            # Find all phone numbers on the page
            phone_pattern = re.compile(r'\b\d{4}[-.]?\d{3}[-.]?\d{4}\b')
            phone_numbers = []
            for match in phone_pattern.findall(soup.get_text()):
                phone_numbers.append(match)
        
            [errors.append(number) for number in phone_numbers if number not in self.phone_numbers]
        else:
            errors.append("No phone numbers found")
        
            
        if self.emails:
            # Find all email addresses on the page
            email_pattern = re.compile(r'\b[\w.-]+@[\w.-]+\.\w{2,}\b')
            email_addresses = []
            for match in email_pattern.findall(soup.get_text()):
                email_addresses.append(match)

            [errors.append(email) for email in email_addresses if email not in self.emails]
        else:
            errors.append("No email addresses found")
        
        if errors:
            status = False
        else:
            errors=["Contact details correct"]

        self.echo(status,errors)
        # return status, errors

    def send_report(self):
        if t.report and push:
            pb.push_note(self.url+" Alert", self.report)
        else:
            pb.push_note("Operational")
            
    
    def check_website(self):
        """
        Checks the webpage loads
        """
        response, status_code, status = self.request_handler(self.url)   
        self.echo(status, self.errors)
         # Print the load time in seconds
        print("Load time for", self.url, ":",self.load_time[self.url], "seconds")
 

    def check_links(self):
        print("Checking links @ "+self.url)
        # Get the website's HTML content
        response, status_code, status = self.request_handler(self.url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all links on the page
        links = soup.find_all("a")

        # Loop through each link and check if it loads without error
        for link in links:

            href = link.get("href")
            if href:
                if href.startswith("http"):
                    link_response, status_code, status = self.request_handler(href)
                    self.process_status_code(href,status_code)

                    if status is True:
                        # Print the load time in seconds
                        try:
                            print("Load time for", href, ":", self.load_time[href], "seconds")
                        except Exception as e:
                            pass
                    else:
                        self.echo(False, link)
        
        print("Checking script links @ "+self.url)
        script_urls=[]
        for script in soup.find_all('script'):
            script_text = script.string
            if script_text:
                pattern = re.compile(r'(?P<url>https?://[^\s<>"]+|www\.[^\s<>"]+)')
                script_urls = re.findall(pattern, script_text)

            if script_urls:
                for href in script_urls:
                    link_response, status_code, status = self.request_handler(href)
                    self.process_status_code(href,status_code)
                                        
                    if status is True:
                        # Print the load time in seconds
                        try:
                            print("Load time for", href, ":", self.load_time[href], "seconds")
                        except Exception as e:
                            pass
                    else:
                        self.echo(False, link)

    def check_domain(self):
        # Get WHOIS information for the domain
        w = whois.query(self.url)

        # The expiration date of the domain
        expiration_date = w.expiration_date
        
        # The current nameservers
        nameServers = w.name_servers

        # Nameserver Tests
        for x in self.name_servers:
            if x in nameServers:
                # print(x)
                self.echo(True, "The domain "+self.url+" is using nameserver "+x)
            else:    
                self.echo(False, "The domain "+self.url+" has an incorrect nameserver "+x)

        if nameServers:
            self.echo(False, "Nameservers "+str(nameServers)+" do not match specification for "+self.url)
        
        # Domain Renewal
        for x in ["expire","expiration"]:
            if x in nameServers:
                self.echo(False, "The domain "+self.url+" has already expired!")
                return
        

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

    urls = [["http://www.boejaker.com",["abby.ns.cloudflare.com","brad.ns.cloudflare.com"],["jb.enquiries@proton.me"],["07761544030"]],\
            ["http://www.maxhodl.com",["ns1.dns-parking.com","ns2.dns-parking.com"],["jb.enquiries@proton.me"],["07761544030"]],\
            ["http://boejaker.github.io",['dns1.p05.nsone.net', 'dns2.p05.nsone.net', 'dns3.p05.nsone.net', 'ns-1622.awsdns-10.co.uk', 'ns-692.awsdns-22.net'],["jb.enquiries@proton.me"],["07761544030"]]]

    print(f"Testing {len(urls)} urls, {urls}")
    
    for u, name_servers, emails, phone_numbers in urls:
        
        t=test(u, name_servers, emails, phone_numbers) # TODO Create threads for each website here

        print(f"Analyzing website {u}")

        t.check_website()
        t.check_domain()
        t.check_links()
        t.find_contacts()

        t.send_report()
        print(t.report)
        print(f"pass {t.pass_count}/{t.total} failed{t.fail_count}/{t.total}")
    
    # TODO Join threads for each website here

