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

from decouple import config

from pushbullet import Pushbullet

pb = Pushbullet(config('pb_api'))

report = ""

pass_count=0
fail_count=0
class test():
    def echo(self, status, output):
        global report
        global pass_count
        global fail_count
        if status is True:
            print(f"\033[32m\u2714 {output} \033[0m")
            pass_count+=1
        if status is False:
            print(f"\033[91m\u2717 {output} \033[0m")
            report += str(output)+"\n"
            fail_count+=1
        

    def find_contacts(self, url):
        print("Checking contact details @ "+url)
        status = True
        response = requests.get(url)
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


        return status, errors

    def send_report(self, url, report):
        push = pb.push_note(url+" Alert", report)    

    def read_status(self, url):
        """
        Reads the uptime file of a website
        """
        status = False
        output=url+" domain is inactive"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
            
        if soup.find(id='ActiveDomain'):
            status = True
            output=url_+" domain is active"
        
        # If no keywords are found, assume it's not a parked domain
        return status, output
    
    def check_website(self, url):
        print("Checking @ "+url+" is online")
        """
        Checks the webpage loads
        """
        status = False
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            output = url+" is up and running with status code "+str(response.status_code)
            status = True
        except requests.HTTPError as http_error:
            output = url+" is offline with HTTP error: "+str(http_error)
        except requests.ConnectionError as connection_error:
            output = url+" is offline with connection error:  "+str(connection_error)
        except requests.Timeout as timeout_error:
            output = url+" is offline with timeout error:  "+str(timeout_error)
        except requests.RequestException as request_exception:
            output = url+" is offline with unknown exception:  "+str(request_exception)

        return status, output

    def check_links(self, url):
        print("Checking links @ "+url)
        # Get the website's HTML content
        response = requests.get(url)
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
        
        print("Checking script links @ "+url)
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

    def check_source(self):
        """
        Checks the loaded page matches the source
        """
        pass

if __name__ == "__main__":

    urls = ["http://www.boejaker.com","http://www.maxhodl.com","http://boejaker.github.io"]

    print(f"Testing {len(urls)} urls, {urls}")
    
    for u in urls:

        t=test()

        pass_count=0
        fail_count=0

        total=lambda fail_c, pass_c: fail_c+pass_c
        report = ""
        print(f"Analyzing website {u}")

        # status, output = t.read_status(u)
        # t.echo(status, output)

        t.check_links(u)

        status, output = t.find_contacts(u)
        t.echo(status, output)

        if report:
            # pass
            t.send_report(u,report)
        else:
            # pass
            t.send_report(u,"Operational")
        total=total(fail_count, pass_count)
        print(f"pass {pass_count}/{total} failed{fail_count}/{total}")


