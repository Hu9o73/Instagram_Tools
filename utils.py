from bs4 import BeautifulSoup


def getFollowers(dir="./"):
    '''
    Retrieve the list of your followers as an array.\n
    Pass the filepath to your instagram's data (relative to this script). (instagram-username folder)\n
    Don't forget the "/" at the end of the filename.
    '''
    file_path = dir + "connections/followers_and_following/followers_1.html"
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    a6_p_divs = soup.find_all('div', class_='_a6-p')
    names = [div.find('a').text for div in a6_p_divs if div.find('a')]

    return names

def getFollowing(dir="./"):
    '''
    Retrieve the list of the people you follow as an array.\n
    Pass the filepath to your instagram's data (relative to this script). (instagram-username folder)\n
    Don't forget the "/" at the end of the filename.
    '''
    file_path = dir + "connections/followers_and_following/following.html"
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    a6_p_divs = soup.find_all('div', class_='_a6-p')
    names = [div.find('a').text for div in a6_p_divs if div.find('a')]

    return names

