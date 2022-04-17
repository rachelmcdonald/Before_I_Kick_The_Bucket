#First CodeClan Project: A Travel Bucket List Web Application

##Set Up

###To Run the Application:
- cd into 'travel_bucketlist_project' and the type 'code .' to open in the code editor.
- With the 'travel_bucketlist_python_project' file opened in VSCode, open your terminal and run 'flask run'.
- CMD + click on the link that appears within the terminal to view the application on a local host within your browser.


##Project Brief:

Travel Bucket List
Build an app to track someone's travel adventures.

MVP:
- The app should allow the user to track countries and cities they want to visit and those they have visited.
- The user should be able to create and edit countries
- Each country should have one or more cities to visit
- The user should be able to create and delete entries for cities
- The app should allow the user to mark destinations as visited or still to see

Possible Extensions:
- Have separate pages for destinations visited and those still to visit
- Add sights to the destination cities
- Search for destination by continent, city or country
- Any other ideas you might come up with


All MVP points were reached with everything working as intended within the browser.
I will come back and update with extensions when I have some more time after the course.

##Technologies:
- Flask
- psycopg2
- SQL
- Python
- HTML
- CSS
- VSCode as the code editor


##Brief description of my project:
Starting with the homepage, I created a minimalist feel navigation bar that was consistent through out my application
and gave the styling a hover effect with a .5s delay so when the user hovered over the tab, it gave a visual
queue that this was a clickable object.
<img width="500" alt="Screenshot 2022-02-10 at 16 50 04" src="https://user-images.githubusercontent.com/64783968/153457363-296e8d43-c1dd-464b-bd1a-3b3b0cabe09c.png">

Within the contents of the home page, I created two buttons that allow the user to view their countries and cities on
separate pages. I added a hover effect that turned the colour of the button slightly transparent as well as changing the
cursor to "pointer" in CSS so that when hovered over, this would be clear that it was a call-to-action button.
<img width="501" alt="Screenshot 2022-02-10 at 17 01 47" src="https://user-images.githubusercontent.com/64783968/153458395-a3a8090c-a2a3-4f93-97dc-a8c87bb9e1fd.png">


Within the 'countries' page on the application I stylized each country section with emojis within the HTML code (pin to indicate
location next to the country name). I wanted to allow the user to see if they had visited or were still to visit the country on their list
so within my HTML code I added a Python 'if' statement to view the boolean value in a more user-friendly manner. I gave this section
its own 'id' within HTML so I could focus on that element individually on CSS, where I gave the value a border and coloured both that and
the text green for 'visited' with an emoji checkmark, and orange which represents "pending" for "still to visit" - where I added an emoji of a
briefcase next to that. Each country has been given its own button to either 'delete' or 'edit' the country.
<img width="500" alt="Screenshot 2022-02-10 at 16 51 14" src="https://user-images.githubusercontent.com/64783968/153459822-0f8d92d4-3595-42ae-aae6-f15dc3644e2d.png">
<img width="500" alt="Screenshot 2022-02-10 at 16 51 52" src="https://user-images.githubusercontent.com/64783968/153459756-ec83325f-35e8-41fb-8404-5721b4b7416e.png">
<img width="500" alt="Screenshot 2022-02-10 at 16 52 11" src="https://user-images.githubusercontent.com/64783968/153459912-fb09c8f0-5289-465a-a93a-4d4e451bc0aa.png">
<img width="1158" alt="Screenshot 2022-02-10 at 17 06 02" src="https://user-images.githubusercontent.com/64783968/153461163-5e690165-af0e-42d2-8025-e46f1e1f385a.png">

By either clicking on the "View Cities" button at the bottom of the "Countries" page or by selecting "Cities" in the navigation bar at the top of the screen,
it will take the user to the page where the application displays the list of cities that the user has/is still to visit.
I used the same logic, but for 'cities' rather than 'countries' within my HTML to display the city name and its boolean value, as well as adding 
'city.country.id' where I was able to display the country to which the city belongs. I also added a drop down menu within the 'Cities' page to allow the
user to select a 'country' from the already added 'Countries' page where they wished to link the city to. This was achieved by adding a Python 'for' loop
into the HTML code.
<img width="501" alt="Screenshot 2022-02-10 at 16 52 57" src="https://user-images.githubusercontent.com/64783968/153461677-33c4da4b-bfe7-4361-9774-ddf7683450ad.png">
<img width="497" alt="Screenshot 2022-02-10 at 16 53 10" src="https://user-images.githubusercontent.com/64783968/153461712-011cc93b-6e7d-443e-96fe-25546c0a4ca1.png">
<img width="500" alt="Screenshot 2022-02-10 at 17 02 15" src="https://user-images.githubusercontent.com/64783968/153461752-acc782cd-9c91-4c17-9edf-9ad129a87dcc.png">
<img width="672" alt="Screenshot 2022-02-10 at 17 16 17" src="https://user-images.githubusercontent.com/64783968/153461783-597e8c89-9cb1-45b1-982d-1d3ad92b9ab3.png">



