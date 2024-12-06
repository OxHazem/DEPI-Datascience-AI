from Scrapper import (get_Html_text,get_Url_response,parse_html,finding_Data,converting_into_Csv_file)

def main():
    url = 'https://www.ratemyprofessors.com/search/professors/1452?q=*'
    response=get_Url_response(url)
    text=get_Html_text(response)
    soup=parse_html(text)
    print('----------------------------------\n \n \n')
    teacher_list=finding_Data(soup)
    converting_into_Csv_file(teacher_list)

main()
