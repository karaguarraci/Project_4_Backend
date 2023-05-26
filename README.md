# SEI Project 4 - Pawsome Dining

This solo project involved building a full stack web application, which allowed users to search for dog-friendly restaurants in a particular city. The backend of the project was built using Python and Django, while the frontend was built using React, with additional styling implemented through React-Bootstrap and SASS.
The application includes a search function on the homepage, as well as an "All Restaurants" page and a "My Favourites" page. To utilise certain features of the application, such as adding reviews, updating/deleting reviews, and adding restaurants to a favourites list, users must first register and log in to the platform.

This repo contains code for the backend only. Code for the frontend can be found [here](https://github.com/karaguarraci/Project_4_Frontend)

Check out the live [Pawsome Dining](https://pawsomedining.netlify.app) site.

Feel free to use these credentials to sign in:
- Username: user2@user.com
- Password: Password!1

## Application Visuals

## Tech Stack
#### Frontend
React | React-Router-Dom | Axios | React-Bootstrap | CSS | Sass
#### Backend
Python + Django Rest Framework | PostgreSQL | JSON Web Token (JWT)
#### Development and Deployment
Git | GitHub | Excalidraw | Postman | Npm + Pipenv | Netlify | Heroku

## Project Brief
- Build a full-stack application by making your own backend and your own front-end
- Use a Python Django API - using Django REST Framework to serve your data from a Postgres database
- Consume your API with a separate front-end built with React
- Be a complete product - which most likely means multiple relationships and CRUD functionality for at least a couple of models
- Implement thoughtful user stories/wireframes 
- Have a visually impressive design 
- Be deployed online so it's publicly accessible.
- React Hooks is optional for this project

## Timeframe
3 Weeks | Solo project

## Planning 
At the start of the project, I used Excalidraw to create a plan for the layout and functionality of the application, including any potential stretch goals. From there, I focused on developing the backend API. I began by planning out the necessary models and apps, as well as the relationships between them. This helped me determine where I needed to retrieve and display various types of information, and what to include in each app's populated serializer. This planning process helped me to conceptualise how to link the backend and frontend in order to develop the application as I had envisioned it.

<img src="https://github.com/karaguarraci/Project_4_Frontend/assets/115991254/13049926-1cae-4a85-a647-6f071aef531f" alt="project wireframe" width="500">

##Build/Code Process
### Creating the Backend
During the backend development phase of my project, I focused on creating four separate apps: "restaurants," "dog_friendly," "jwt_auth," and "reviews." I planned out the initial data fields required for each model.
In the "restaurants" model, I included fields such as "name," "address," "website," and "location" (later refined to "city"). To handle dog-friendliness, I decided to incorporate a Boolean field directly in the "restaurants" model and use the "dog_friendly" model to store additional amenities, such as: “provides_treats”, “has_doggy_menu”.
For the "User" model, I initially included the "email" and "favourites" fields. However, as development progressed, I realised the need for a separate "favourite" model to manage user favourites effectively.
In the "Reviews" model, I included fields for "rating," "comment," and "created_by." 
In the “Favourites” model, which I added later on, I included fields for “restaurant” and “owner”.

During the planning stage, I had determined the relationships between the different apps and the information I wanted to display. I considered whether these relationships would be one-to-many or one-to-one.
To showcase the linked data effectively, I created populated serializers. These serializers allowed me to display information from connected apps by establishing relationships and including relevant fields.
For example, in the relationship between the "restaurants" and "reviews" apps, I wanted to show the reviews for each restaurant. I set up a one-to-many relationship, where each restaurant can have multiple reviews. By adding a foreign key field named "restaurant”, with a related name of “reviews” in the "reviews" model and importing the "ReviewSerializer" into the "PopulatedRestaurantSerializer," I was able to display the associated reviews for each restaurant. By carefully defining the relationships between the models, I ensured that I could retrieve and display relevant reviews when accessing either all restaurants or a specific restaurant.
```py
class Review(models.Model):
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE, related_name='reviews')
    favourites = models.ForeignKey('favourites.Favourite', null=True, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'jwt_auth.User', 
        related_name='reviews', 
        on_delete=models.CASCADE)
 ```
 ```py
 class PopulatedRestaurantSerializer(RestaurantSerializer):
    dog_friendly = DogFriendlySerializer()
    reviews = ReviewSerializer(many=True)
    favourites = FavouriteSerializer(many=True)
```

## Creating the Frontend

During the planning phase, I had made the decision to create an "allRestaurants" page where users could browse through all the dog-friendly places. To style the page, I opted to use React-Bootstrap cards. Within each card, I included the restaurant image, name, average rating, and city. Additionally, I added a button that, when clicked, would direct the user to the specific page of that restaurant.
To fetch the necessary data and populate the cards, I utilised the axios.get method. By making the appropriate API call, I retrieved the restaurant information. To display the fetched data, I utilised the map function to iterate through all the restaurants. For each restaurant, I extracted the desired fields and rendered them in the card component.
This approach allowed me to create an "allRestaurants" page with visually appealing cards, displaying relevant information about each dog-friendly restaurant. Users can easily navigate to individual restaurant pages by clicking the provided buttons.

After completing the "allRestaurants" page, my focus shifted towards populating the "single restaurantPage" with more detailed information about a specific restaurant. I aimed to include additional details such as the restaurant's description, address, and a link to their website. Moreover, I wanted to display the restaurant's reviews and extra dog-friendly information on this page as well.
To accomplish this, I had already prepared the backend by adding the necessary fields to the "PopulatedRestaurantSerializer." This serializer contained all the information required to populate the single restaurant page.
By making a GET request for a specific restaurant, I could retrieve the relevant data from the backend. The "PopulatedRestaurantSerializer" enabled me to render this information onto the restaurant's individual page, presenting the description, address, and website link. Furthermore, I could display the restaurant's reviews and any additional dog-friendly information by utilising the existing data within the serializer.
Through these implementations, I successfully populated the single restaurant page with details about the restaurant, including its description, address, website link, reviews, and extra dog-friendly information.

To enable the current user to add a review to a restaurant, I implemented a form that would facilitate the review submission process. Initially, the form was hidden, and I used useState to control its visibility. When the user clicked the "add review" button, the state would be updated, causing the form to be displayed.
Within the form, I included relevant input fields such as the rating and review text. Upon submitting the form, I implemented a POST request to send the review data to the backend. This request would add the review to the respective restaurant.

```js
 const onSubmit = async (e) => {
    // e.preventDefault();
    try {
      const token = localStorage.getItem("token");
      console.log(token);
      const restaurantId = singleRestaurantInfo.id;
      const addedReview = await axios.post(
        `${API_URL}/reviews/`,
        { ...formData, restaurant: restaurantId },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
      console.log(addedReview);
      if (addedReview) {
        setShowForm(false);
      }
    } catch (err) {
      console.log("post not worked");
      console.log(err);
    }
  };
```
  
To enable users to update and delete their reviews, I implemented functionalities that ensured the corresponding buttons were visible only for reviews they had created. By checking for a logged-in user and comparing their unique identifier with the review owner, I selectively displayed the buttons.

```js
{loggedInUser && loggedInUser.sub === review.owner ?
```
For updating a review, I used the useState hook to manage the form's state. The initialFormData, which contained the current review data, pre-filled the form with the existing rating and comment. Clicking the "update" button updated the state, revealing the form for users to modify their rating and comment. Upon submission, a PUT request was sent to the backend to update the review accordingly.

```js
 const onSubmit = async (e) => {
    try {
      const token = localStorage.getItem("token");
      const reviewId = review.id;
      const updatedReview = await axios.put(
        `${API_URL}/reviews/${reviewId}/`,
        { ...formData },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
      console.log(updatedReview);
      setShowEditForm(false);
    } catch (err) {
      console.log(err);
    }
  };
 ```
To delete a comment, I implemented an onDelete function that triggered a DELETE request to the backend when the corresponding button was clicked.
With these implementations, users can conveniently update and delete their own comments, while ensuring the buttons are only visible for the comments they have created.

```js
  const onDelete = async (e) => {
    try {
      const token = localStorage.getItem("token");
      const reviewId = review.id;
      const reviewToDelete = await axios.delete(
        `${API_URL}/reviews/${reviewId}/`,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
      window.location.reload();
      console.log(reviewToDelete);
    } catch (err) {
      console.log(err);
    }
  };
 ```
 
 As users can include a rating with their reviews, I wanted to add the average rating to all of the restaurants.  To calculate the average rating for restaurants based on their reviews, I implemented a function called calcAv in the frontend. This function takes the reviews array as an input parameter.
First, I check if the reviews array exists. If it doesn't, I return a default value of 0.
Next, I initialise totalscore to 0, which will keep track of the cumulative score from all the reviews, and totalCount to the length of the reviews array, representing the total number of reviews.
Using Array.from(reviews).forEach, I iterate over each review in the reviews array. Inside the loop, I add up the rating value from each review to the totalscore variable.
Once I have iterated through all the reviews, I calculate the average score by dividing totalscore by totalCount and store the result in avgScore. To round the average score to one decimal place, I multiply avgScore by 10, round it using Math.round, and then divide by 10 again.
Finally, the function returns the calculated average score.
By utilising the calcAv function, I can determine the average rating for a collection of reviews. This allows me to display the average rating for each restaurant based on their reviews.

```js
export function calcAv(reviews) {
  if (!reviews) {
    return 0;
  }
  let totalscore = 0;
  let totalCount = reviews.length;
  Array.from(reviews).forEach((review) => {
    totalscore += review.rating;
  });
  let avgScore = totalscore / totalCount;
  return Math.round(avgScore * 10) / 10;
}
```
To allow users to add a restaurant to the database, I created an "AddRestaurant" page in my application. I used the useState hook from React to manage the form state and render the necessary inputs on the page.
The initial state for the form data includes fields such as the restaurant's name, city, address, description, image, website, and a checkbox indicating whether it is dog-friendly.
For the form inputs, I implemented an onChange function that updates the form data state whenever the user makes changes to any input field. This allows the form values to be dynamically updated as the user types.
To handle the form submission, I defined an onSubmit function that is triggered when the user clicks the "Add" button. Inside this function, I make a POST request and I include the form data in the request payload and also send the user's token in the request headers for authentication.
In the return statement, I render the form components using React Bootstrap. Each input field is associated with the corresponding form data state value and includes an onChange event handler to update the form data state when the user interacts with the inputs.
Finally, the form includes an "Add" button that triggers the form submission when clicked.

<img src="https://github.com/karaguarraci/Project_4_Frontend/assets/115991254/74e2db50-4c17-49e9-b3b5-4eeac64c7dd0" alt="app screenshot" width="250">

After successfully adding a restaurant, I noticed an issue when attempting to access the restaurant's page. The problem occurred because the restaurant didn't have any reviews associated with it yet. To address this, I implemented a condition to check if there were any reviews available for the restaurant. If there were reviews, I displayed the average rating using the ReactStars component. However, if there were no reviews, I displayed the message "No reviews yet".

```js
  {singleRestaurantInfo.reviews.length > 0 ? (
                  <ReactStars
                    className="rating-stars"
                    count={5}
                    value={calcAv(singleRestaurantInfo.reviews)}
                    size={24}
                    edit={false}
                    isHalf={true}
                    activeColor="#ffd700"
                  />
                ) : (
                  "No reviews yet"
                )}
```

In this code snippet, I'm checking the length of the reviews array associated with the singleRestaurantInfo object. If the length is greater than zero, indicating that there are reviews available, I render the ReactStars component to display the average rating. The calcAv function is used to calculate the average rating based on the available reviews. However, if the length is zero, I display the "No reviews yet" message instead.
This implementation ensures that users visiting a restaurant's page will see the appropriate information depending on whether there are reviews or not.

In the RestaurantCard component, I implemented the functionality to add dog-friendly extras to a restaurant. The process begins when the user clicks the "Add" button under the prompt "Add dog friendly extras?". This button is only visible if no extras have been added yet.
When the button is clicked, the handleClick function is triggered. It updates the state variable showDogInfoForm to true, which controls the visibility of the dog-friendly extras form. Additionally, it initialises the dogInfoFormData state with default values.
The form is rendered conditionally based on the showDogInfoForm state. If showDogInfoForm is true, the form is displayed, allowing the user to input dog-friendly information. The user can select checkboxes for options like providing water bowls, providing treats, and having a doggy menu. There's also a text input field for additional doggy extras.
When the user submits the form, the handleSubmit function is called and it sends a POST request to the server to add the dog-friendly information for the restaurant. The axios.post method is used with the appropriate endpoint and data. Upon successful submission, the showDogInfoForm state is set to false, hiding the form.
If there are already dog-friendly extras associated with the restaurant, the existing information is displayed instead of the form. It shows whether the restaurant provides water bowls, treats, and has a doggy menu. Additionally, it displays any additional doggy extras that were previously added. Overall, this implementation allows users to add and view dog-friendly extras for a restaurant. It provides a user-friendly interface to input the information and ensures the data is stored correctly in the backend.

## Challenges
Building the search bar was a challenge because I needed to implement a feature that allows users to search for restaurants based on a specific city. Here's how I resolved it:
First, I created a separate SearchBar component. This component receives the onSearch function as a prop, which will be triggered when the user submits the search form. The search form consists of a text input field for the city name and a submit button.

```js
const SearchBar = ({ onSearch }) => {
  return (
    <Container className="mt-5" onSubmit={onSearch}>
      <Row>
        <Col sm={4} style={{ width: "100%" }}>
          <Form className="d-flex">
            <Form.Control
              type="search"
              placeholder="Search for a city..."
              className="me-2"
              onChange={onSearch}
              name="city"
            />
            <Button className="button search-button">Search</Button>
          </Form>
        </Col>
      </Row>
    </Container>
  );
};
```

In the Home page, I imported and used the SearchBar component. Inside the onSearch function, I filter the restaurantCardData state array based on the city name entered by the user. The filtered restaurants are stored in the filteredRestaurants variable.
I then use the navigate function from the react-router-dom package to navigate to the /city route with the lowercase city name as the URL parameter. I also pass the filtered restaurants as the state object to the new route. This allows me to access the filtered restaurants in the City component.

```js
 const onSearch = (e) => {
    const filteredrestaurants = restaurantCardData.filter((restaurant) =>
      restaurant.city.toLowerCase().includes(e.target.value.toLowerCase())
    );
    console.log(filteredrestaurants);
    navigate(`/city/${e.target.value.toLowerCase()}`, {
      state: filteredrestaurants,
    });
    setCardsToDisplay(filteredrestaurants);
  };
 ```
 
In the City component, I use the useLocation hook from react-router-dom to access the state object passed from the previous route. I console.log the state to verify that I received the filtered restaurants correctly.
Finally, I map through the state array and render the AllRestaurantsCard component for each restaurant, passing the restaurantData prop with the corresponding restaurant object.
By breaking down the functionality into separate components and utilising the useLocation hook, I was able to implement the search bar feature successfully. Users can search for a city, and the application will display the restaurants that match the search criteria in the City component.

```js
const City = () => {
  const { state } = useLocation();
  console.log(state);

  return (
    <div>
      <div className="city-card">
        {state.map((restaurant) => (
          <AllRestaurantsCard key={restaurant.id} restaurantData={restaurant} />
        ))}
      </div>
    </div>
  );
};
```
## Wins

- I'm really pleased with how my project turned out, especially when it comes to making it mobile responsive. In the past, I struggled with implementing responsiveness in my projects, but this time I was able to overcome those challenges. Bootstrap played a significant role in achieving this, as its responsive grid system and pre-built components made it much easier for me to create a responsive layout.
- I am extremely proud of my accomplishment in building a full-stack application as a solo project within a three-week timeframe. It was challenging and required a combination of technical skills, problem-solving abilities, and efficient time management.

## Key Learnings
- Python: This project served as a valuable opportunity for me to strengthen my understanding of Python. As it was my first project using the language, I was able to delve into its fundamentals and solidify my knowledge. By actively applying Python concepts and techniques throughout the development process, I gained a deeper understanding of the language and its functionalities.
- Solo project pros and cons: Taking on the final project alone had its ups and downs. Although I missed working collaboratively, going solo allowed me to further develop my skills and build a full-stack app independently. Overcoming challenges boosted my confidence and provided valuable learning opportunities.

## Known Bugs
- I encountered a challenge while adding restaurants to the favourites page. After adding a restaurant, I noticed that it no longer had any reviews associated with it. This issue was not limited to the frontend, as I confirmed it while testing the backend using Postman. Despite my efforts, I couldn't determine the exact cause of this problem. As a result, the added restaurants on the favourites page were missing their reviews. I tried to investigate the issue further, but I have so far been unable to identify the specific issue in the backend code that caused the reviews to be omitted.
- When attempting to register, there is an error message stating that the "favourites" field is required. Unfortunately, I haven't been able to find a solution to fix this issue yet.

## Future Improvements
- Ability for users to update and delete the restaurants they have added.
- Enhance the favourites page to display filled heart icons for favourite restaurants.
- Implement the ability to remove a restaurant from the favourites list by clicking on the filled heart. 

