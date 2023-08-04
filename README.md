# social_media_app<br>
#### Built APIs for a social media platform in Python django.<br>
#### The API should support features like getting a user profile, follow a user, upload a post, delete a post, like a post, unlike a liked post, and comment on a post.<br>

### **API Endpoints**<br>

- POST /api/authenticate should perform user authentication and return a JWT token.<br>
    - INPUT: Email, Password<br>
    - RETURN: JWT token<br>
- POST /api/follow/{id} authenticated user would follow user with {id}<br>
- POST /api/unfollow/{id} authenticated user would unfollow a user with {id}<br>
- GET /api/user should authenticate the request and return the respective user profile.<br>
    - RETURN: User Name, number of followers & followings.<br>
- POST api/posts/ would add a new post created by the authenticated user.<br>
    - Input: Title, Description<br>
    - RETURN: Post-ID, Title, Description, Created Time(UTC).<br>
- DELETE api/posts/{id} would delete post with {id} created by the authenticated user.<br>
- POST /api/like/{id} would like the post with {id} by the authenticated user.<br>
- POST /api/unlike/{id} would unlike the post with {id} by the authenticated user.<br>
- POST /api/comment/{id} add comment for post with {id} by the authenticated user.<br>
    - Input: Comment<br>
    - Return: Comment-ID<br>
- GET api/posts/{id} would return a single post with {id} populated with its number of likes and comments<br>
- GET /api/all_posts would return all posts created by authenticated user sorted by post time.<br>
    - RETURN: For each post return the following values<br>
        - id: ID of the post<br>
        - title: Title of the post<br>
        - desc: Description of the post<br>
        - created_at: Date and time when the post was created<br>
        - comments: Array of comments, for the particular post<br>
        - likes: Number of likes for the particular post<br>
