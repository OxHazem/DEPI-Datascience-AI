import requests 
from bs4 import BeautifulSoup 
import pandas 

quality_ids = [
     'CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 bUneqk',
     'CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 gcFhmN',
     'CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 icXUyq'
]


def  get_Url_response (Url): # to check for the URL response
    response= requests.get(Url)
    print(response)
    return response

def get_Html_text(response):
    text= response.text
    return text

def parse_html(html_text):
    soup= BeautifulSoup(html_text, 'html.parser')
    print('HTML Parsed successfully')
    print(soup.prettify())
    return soup 


def finding_Data (soup):
        teacher_data=soup.find_all('a',class_='TeacherCard__StyledTeacherCard-syjs0d-0 dLJIlx')
        teacher_list=[]
        quality_ids = [
     'CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 bUneqk',
     'CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 gcFhmN',
     'CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 icXUyq'
    ]
        for data in teacher_data :
            teacher_div_data={}
            name=data.find('div',class_='CardName__StyledCardName-sc-1gyrgim-0 cJdVEK')  
            teacher_div_data['name']=name.text.strip()

            depatment=data.find('div',class_='CardSchool__Department-sc-19lmz2k-0 haUIRO')  
            teacher_div_data['department']=depatment.text.strip()

            school=data.find('div',class_='CardSchool__School-sc-19lmz2k-1 iDlVGM')
            teacher_div_data['school']=school.text.strip()

            Feedback=data.find('div',class_='CardFeedback__CardFeedbackNumber-lq6nix-2 hroXqf')  
            teacher_div_data['Feedback']=Feedback.text.strip()

            Quality_points = None
            teacher_div_data['Quality_points']= None
            for id in quality_ids:
                if Quality_points is not None:
                    break
                try:
                    Quality_points=data.find('div',class_=id)
                    teacher_div_data['Quality_points']= Quality_points.text.strip()
                except:
                    pass
            #print(teacher_div_data['Quality_points'])
                      
            Number_Ratings=data.find('div',class_='CardNumRating__CardNumRatingCount-sc-17t4b9u-3 jMRwbg')
            teacher_div_data['Number_Ratings']=Number_Ratings.text.strip()

            teacher_list.append(teacher_div_data)
        print(teacher_list)
        return teacher_list
def converting_into_Csv_file(teacher_list):
    df = pandas.DataFrame(teacher_list)
    df.to_csv('D:\DownLoad\learining courses\DEPI-DS-AI\Projects\webscrapping\Project 1\data\RateMyProfessors.csv', index=False)
    print('CSV file created successfully open data folder') 
 

    






