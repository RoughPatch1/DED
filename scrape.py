from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

dir_path = 'Links/'
for file in os.listdir(dir_path):
    if file.endswith(".txt"):
        file_path = f"{dir_path}{file}"
    else:
        continue
    # print("---------------------------------------------------------------------------------")
    # print(file_path)
    # print("-------------------------------------------------------------------------------------")
    with open(file_path,'rt') as lines:
        df=pd.DataFrame()
        while True:
        # Get next line from file
            line = lines.readline()
    
        # if line is empty
        # end of file is reached
            if not line:
                break
            print("'''''''''''''''''''",str(line))
            response = requests.get(line).text
            soup = BeautifulSoup(response, 'html.parser')
            name = soup.find('title').text
            print(name)
            descfil = soup.find('div', class_= 'vue--markdown-to-html markdown-description')
            descfil2 = descfil.find('p')
            affectpkg = descfil.find('code').text
            descfil3 = descfil2.find_next('p')
            desc = descfil3.find_next('p').text
            CVElink = soup.find('span', class_= 'cve')
            ref = CVElink.find('a', href=True)
            link2 = str(ref['href'])
            # # Find the attack complexity
            # attack_complexity1 = soup.find('div', class_='cvss-details-item')
            # attack_complexity = attack_complexity1.find('strong').text
            # # Find the confidentiality impact
            # confidentiality1 = soup.find_next('div', class_='cvss-details-item')
            # confidentiality = confidentiality1.find('strong').text
            # # Find the integrity impact
            # integrity = soup.find('span', class_='vuln-card__cvss-integrity').text
            # # Find the availability impact
            # availability = soup.find_next('span', class_='vue--badge__text').text
            # Find the vulnerability name
            
            # Find the vulnerability vector
            # vector = soup.find('div', class_='vuln-card__vector').text
            # avh = soup.find('span', class_='vue--badge vue--badge--high-severity vue--badge--ghost vue--badge--small vue--badge--pill vue--badge--uppercase').text
            # print(avh)
            data = {"Name": [name], "Link": [link2], "Affected Package": [affectpkg], "Description": [desc]}

            df= pd.concat([df,pd.DataFrame(data)])
            # print(df)
            # df.to_excel("ApacheOutput.xlsx")
            # Print the information to the console
            # print(desc)
            # print(link2)
            # print(name)
            # print(affectpkg)
            # print(confidentiality)
            # print(integrity)
            # print(availability)
            # print(name)
            # print(description)
            # print(vector)

    lines.close()
    df=df.reset_index(drop=True)
    file_name = file_path.split('.')[0]+ '.csv'
    df.to_csv(file_name)