import requests
import json

def fetch_codeforces_profile_api(handle):
    url = f"https://codeforces.com/api/user.info?handles={handle}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        if data['status'] != 'OK':
            print(f"API error: {data.get('comment', 'Unknown error')}")
            return None
        
        user = data['result'][0]
        profile_data = {
            'name': user.get('firstName', 'N/A') + ' ' + user.get('lastName', 'N/A'),
            'rank': user.get('rank', 'N/A'),
            'rating': str(user.get('rating', 'N/A')),
            'max_rating': str(user.get('maxRating', 'N/A')),
            'organization': user.get('organization', 'N/A'),
            'location': user.get('city', 'N/A') + ', ' + user.get('country', 'N/A'),
            'contribution': str(user.get('contribution', 'N/A')),
            'friends': str(user.get('friendOfCount', 'N/A')),
            'registration_time': user.get('registrationTimeSeconds', 'N/A'),
            'last_online': user.get('lastOnlineTimeSeconds', 'N/A')
        }
        return profile_data
    except requests.RequestException as e:
        print(f"Error fetching profile via API: {e}")
        return None
    except KeyError as e:
        print(f"Error parsing API response: {e}")
        return None

def print_profile_data(profile_data):
    if not profile_data:
        print("No profile data available.")
        return

    print("=" * 50)
    print("Codeforces Profile Information (via API)")
    print("=" * 50)
    print(f"Name: {profile_data['name']}")
    print(f"Rank: {profile_data['rank']}")
    print(f"Current Rating: {profile_data['rating']}")
    print(f"Max Rating: {profile_data['max_rating']}")
    print(f"Organization: {profile_data['organization']}")
    print(f"Location: {profile_data['location']}")
    print(f"Contribution: {profile_data['contribution']}")
    print(f"Friends: {profile_data['friends']}")
    print(f"Registration Time (Unix): {profile_data['registration_time']}")
    print(f"Last Online (Unix): {profile_data['last_online']}")
    print("=" * 50)

def main():
    name = input()
    handle = name
    profile_data = fetch_codeforces_profile_api(handle)
    print_profile_data(profile_data)

if __name__ == "__main__":
    main()
