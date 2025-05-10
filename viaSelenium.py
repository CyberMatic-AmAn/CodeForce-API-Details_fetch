from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def fetch_codeforces_profile_selenium(handle):
    url = f"https://codeforces.com/profile/{handle}"
    
    options = Options()
    options.headless = False
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36")
    
    try:
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()
        
        profile_data = {}
        # Same parsing logic as before
        name_tag = soup.find('div', class_='user-name-box')
        profile_data['name'] = name_tag.text.strip() if name_tag else 'N/A'
        
        rank_tag = soup.find('span', class_='user-rank')
        profile_data['rank'] = rank_tag.text.strip() if rank_tag else 'N/A'
        
        rating_tag = soup.find('div', class_='user-rating')
        if rating_tag:
            rating = rating_tag.find('span', class_='rating-number')
            profile_data['rating'] = rating.text.strip() if rating else 'N/A'
        else:
            profile_data['rating'] = 'N/A'
        
        max_rating_tag = soup.find('span', class_='smaller')
        profile_data['max_rating'] = max_rating_tag.text.strip() if max_rating_tag else 'N/A'
        
        org_tag = soup.find('div', class_='user-organization')
        profile_data['organization'] = org_tag.text.strip() if org_tag else 'N/A'
        
        location_tag = soup.find('div', class_='user-city')
        profile_data['location'] = location_tag.text.strip() if location_tag else 'N/A'
        
        contribution_tag = soup.find('div', class_='user-contribution')
        profile_data['contribution'] = contribution_tag.text.strip().replace('Contribution: ', '') if contribution_tag else 'N/A'
        
        friend_tag = soup.find('div', class_='user-friends')
        profile_data['friends'] = friend_tag.text.strip().replace('Friends: ', '') if friend_tag else 'N/A'
        
        reg_time_tag = soup.find('div', class_='user-registration')
        profile_data['registration_time'] = reg_time_tag.text.strip().replace('Registered: ', '') if reg_time_tag else 'N/A'
        
        last_online_tag = soup.find('div', class_='user-last-online')
        profile_data['last_online'] = last_online_tag.text.strip().replace('Last visit: ', '') if last_online_tag else 'N/A'
        
        return profile_data
    except Exception as e:
        print(f"Error fetching profile with Selenium: {e}")
        return None

def print_profile_data(profile_data):
    if not profile_data:
        print("No profile data available.")
        return

    print("=" * 50)
    print("Codeforces Profile Information (via Selenium)")
    print("=" * 50)
    print(f"Name: {profile_data['name']}")
    print(f"Rank: {profile_data['rank']}")
    print(f"Current Rating: {profile_data['rating']}")
    print(f"Max Rating: {profile_data['max_rating']}")
    print(f"Organization: {profile_data['organization']}")
    print(f"Location: {profile_data['location']}")
    print(f"Contribution: {profile_data['contribution']}")
    print(f"Friends: {profile_data['friends']}")
    print(f"Registration Time: {profile_data['registration_time']}")
    print(f"Last Online: {profile_data['last_online']}")
    print("=" * 50)

def main():
    handle = input("Enter the user name : ")
    profile_data = fetch_codeforces_profile_selenium(handle)
    print_profile_data(profile_data)

if __name__ == "__main__":
    main()
