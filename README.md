# Findit Berlin ! 

Welcome to Findit Berlin!
Findit Berlin is your ultimate destination for exploring and documenting street art in the vibrant city of Berlin. This Django-based blog empowers users to engage with Berlin's street art scene in various ways.
Findit Berlin offers a simple and intuitive platform for street art lovers to connect and discover new artworks across the city. Whether you're a seasoned enthusiast or new to the scene, Findit Berlin is your gateway to exploring Berlin's vibrant street art culture.
Join us today and become part of a thriving community passionate about uncovering the hidden gems of Berlin's street art scene!

[Am I responsive]()
---

### Project Goals

#### Objective 

Explore Berlin's vibrant street art scene, brimming with new and emblematic pieces. Findit Berlin is a photoblog crafted to invite street art enthusiasts to share their favorite works, while also serving as a platform to discover new and ongoing emerging interventions."

#### Site users goals 

Create an account to unlock full access to Findit Berlin's features.
Create, Edit, and Delete Posts: Share your favorite graffiti artworks with the community. Add descriptions to provide context and insights about the art.
Commenting and Liking: Engage with fellow street art enthusiasts by leaving comments and expressing appreciation through likes.
Interactive Dashboard: Upon logging in, users are greeted with an interactive dashboard. From here, they can manage their posts effortlessly. This includes listing, editing, and deleting posts, as well as leaving new comments directly from the dashboard.

---

## Agile Developement Methodology 

Agile methodology, rooted in the Agile Manifesto, transforms product development by prioritizing incremental delivery, frequent customer feedback, and adaptability. It addresses the shortcomings of traditional waterfall approaches by breaking projects into smaller, manageable iterations called sprints, fostering quicker response to evolving requirements. Agile extends its applicability beyond software development to various industries, emphasizing responsiveness to market needs and customer demands. It encompasses methods like Scrum, XP, and Kanban, along with technical practices like DevOps, facilitating efficient delivery processes. The Agile Manifesto, established in 2001, articulates core values and principles for software development, serving as a guiding beacon for agile practitioners worldwide.
![Agile Diagram]()



### 12 Agile Manifesto Principles:

* Customer satisfaction through early and continuous delivery of valuable software.
* Embrace changing requirements for the customer's competitive advantage.
* Deliver working software frequently, preferably in shorter timescales.
* Daily collaboration between businesspeople and developers.
* Build projects around motivated individuals, providing them with the necessary support.
* Face-to-face conversation is the most efficient way to convey information within a team.
* Working software is the primary measure of progress.
* Promote sustainable development for long-term success.
* Continuous attention to technical excellence and good design enhances agility.
* Simplicity is crucial; maximize work not done.
* Self-organizing teams produce the best architectures, requirements, and designs.
* Regular reflection and adaptation to improve effectiveness.

### Popular Agile Methodologies:
* Scrum
* Extreme Programming (XP)
* Adaptive Software Development (ASD)
* Dynamic Software Development Method (DSDM)
* Feature Driven Development (FDD)
* Kanban
* Behavior Driven Development (BDD)

This project was developed using Github Kanbanboard [here]() 
Kanban is an Agile management method built on a philosophy of continuous improvement, where work items are “pulled” from a product backlog into a steady flow of work. The framework is applied using Kanban boards, a form of visual project management. In a Kanban board, tasks—represented as cards—move through stages of work—represented as columns. That way, your team can see where work is in real-time.

Kanban is especially popular with product, engineering, and software development teams. But any team that wants to create a more dynamic, flexible workflow can use them.

Kanban teams use a visualization tool called Kanban boards to manage their workload and flow.

In a Kanban board, work is displayed on a project board that is organized by columns. Traditionally, each column represents a stage of work. The most basic Kanban board might have columns like “To do,” “In progress,” and “Done.” Each column is filled with visual cards that represent individual tasks. A team moves through the columns until the tasks are completed.


![MY Kanban board]()

Kanban boards visually represent a team's tasks using cards or sticky notes arranged in columns on a whiteboard. Swimlanes within the columns illustrate the value stream, representing stages tasks must pass through. Cards are placed in the appropriate swimlane to map out the workflow.

As work advances, team members shift cards from left to right. Some swimlanes may have a WIP limit to maintain the system's efficiency.

![4 principles of Kanban]()

### Epics 

### User Stories 
--- 
## Database Schema 

Models used (besides standard user model) in this project are:

*POST* - Post model handles all the Posts created by the users : 
| Field          | Type           | Details                 |
|----------------|----------------|-------------------------|
| title          | CharField      | max_length=100          |
| slug           | SlugField      | max_length=100          |
| author         | ForeignKey     | User, related_name='blog_posts' |
| updated_on     | DateTimeField  | auto_now=True           |
| content        | TextField      | max_length=200          |
| featured_image | CloudinaryField|                         |
| created_on     | DateTimeField  | auto_now_add=True       |
| status         | IntegerField   | choices=STATUS, default=0 |
| likes          | ManyToMany     | Users, related_name='blog_likes', blank=True |
| excerpt        | TextField      | blank=True              |
| favourites     | ManyToMany     | User, related_name='favourites', blank=True |

*COMMENTS* - Comments model handles all the Comments created by the users:
| Field          | Type           | Details                 |
|----------------|----------------|-------------------------|
| post           | ForeignKey     | Post, related_name='comments'         |
| body           | TextField      |           |
| author         | ForeignKey     | User, related_name='author' |
| approved       | BooleanField   | default=False           |
| created_on     | DateTimeField  | auto_now=True       |

*PROFILE* - Profile model handles the Profile creation and editing of Users.
In this model there is a one-to-one relation to the *usermodel* to connect it to the standard user model:
| Field          | Type           | Details                                  |
|----------------|----------------|------------------------------------------|
| user           | OneToOneField  | User, null=True, on_delete=models.CASCADE, related_name='profile' |
| bio            | TextField      |                                          |
| profile_pic    | ImageField     | upload_to='static/images', default='placeholder' |
| instagram_url  | CharField      | max_length=255, null=True, blank=True    |
| website_url    | CharField      | max_length=255, null=True, blank=True    |

![Database Schema]()
---
## UX Design 

### Ux principles 
User Experience (UX) design is a process focused on creating products that offer meaningful and relevant experiences to users. It involves various elements, including branding, design, usability, and functionality, aiming to address users' pain points and needs throughout their journey with the product. While designers cannot control users' perceptions and responses, they can influence how the product behaves and looks.

UX design is user-centered and multidisciplinary, drawing from backgrounds such as visual design, programming, psychology, and interaction design. Designers conduct tasks like user research, creating personas, designing wireframes and prototypes, and testing designs.

### Wireframes 

The site's wireframes were crafted using [Balsamiq](https://balsamiq.com/) software, covering desktop, tablet, and mobile interfaces. While the text content wasn't finalized at that stage, it's important to note some visual variances from the wireframes due to design decisions made during development.

<details>
<summary>Wireframes</summary>
<br>

### Landing Page 
![LandingPage](/static/images/landingpage1.png)

### Post Detail 
![Post Detail](/static/images/postdetail.png)

### Users Dashboard 
![Users Dashboard](/static/images/usersdashboard.png)

</details>

### Site Structure 

The Findit Berlin website is designed with a clear division for users based on their login status.
Whether logged in or out, distinct pages cater to their needs. When logged out, users can only access pages such as 'About,' 'home,' 'Search,' and 'Post Details' 
Upon logging in, additional features including 'Posting,' 'Commenting’, ‘Adding Bookmarks,' and 'Creating a  Profile' become available, enhancing the user experience. 
Further insights into these choices in the 'Features' section.

## Design Choices 

### Color Scheme:

The design of the Findit BERLIN site draws inspiration from the Bootstrap 'light' color theme, fostering a visually appealing environment. Complemented by the subtle accents of Bootstrap Blue for the links, the site achieves a harmonious balance between aesthetics and functionality. Embracing a clean, easy-to-navigate, and minimalistic approach, users are greeted with a seamless browsing experience that enhances their exploration of the platform.
![Light Theme](/static/images/Bootstrapthemelight.png) ![Blue](/static/images/links.png)

### Typography 



## Features 

### Existing Features :

#### Navigation bar

The navigation bar offers a streamlined and intuitive experience. Depending on the user's login status, different menus are presented.

##### For users who are not logged in, the following links are visible:

* About: Provides insights into Findit BERLIN and its creator.
* Home: Directs to the homepage featuring a list of posts, accessible by clicking on the title.
* Register: Navigates to the registration page.
* Login: Offers users the option to log in and access their accounts.

![Nav Bar Big]()
![Nav Bar Small]()

##### All of the links that are visible to a logged in user:
Along with 'Home' 

* User Dashboard: Allows users to navigate through their created posts and add new ones.
* Favorites: Displays all bookmarked posts with options to edit and delete them.
* Profile: Accessible through a dropdown menu, enabling users to visit their profile and edit their profile page.
* Log Out: Allows users to log out of their account.

![Nav Bar Big]()
![Nav Bar Small]()

#### About Page

The About section provides users with insights into Findit BERLIN, offering a glimpse into its purpose and mission. Additionally, users can learn more about the creator behind the platform, gaining a deeper understanding of its origins and vision.

![About]()

#### Landing Maing Page

On the landing page, users, whether logged in or not, can easily access the blog's list of posts. The layout is simple and intuitive, with pagination allowing users to navigate through the blog's content, organized in sets of six posts per page. Each post is displayed as a card, featuring a clickable link to view the post's details. Additionally, users can see the author of each post and the number of likes it has garnered, providing valuable context and engagement opportunities.

![Home]()

#### Users Dashboard


In the user dashboard, each user, including the admin, is greeted with a personalized view showcasing a list of posts they've created. Here, users have the ability to perform actions such as editing or deleting their posts. Each action is accompanied by a warning prompt, ensuring users are informed before proceeding, and a confirmation message informs them of the success or failure of their action.

The admin enjoys exclusive privileges, including the ability to approve, delete, or manage comments across all users' posts. This ensures that the platform maintains high standards of content quality and moderation.

Additionally, users can create new posts directly from the dashboard. If the admin is logged in, posts are instantly published without the need for approval. However, for regular users, a message notifies them that their post is awaiting approval, ensuring transparency and adherence to the platform's guidelines.

![Users Dashboard]()


#### Footer




#### Admin Panel 

#### Registration 

#### Login 

#### Logout 

#### Profile 


---
## Features Left to implement 
---
## Teechnologies Used 
---
## Testing 
---
## Bugs
---
## Deployment 
---
## Credits 
---
## Content 
[Image for jumbotron](https://cdn.pixabay.com/photo/2023/08/05/07/19/berlin-8170586_1280.jpg)

---
## Acknowledgements 

Source Code Links: 
diference between  null=true, blank=true django: https://stackoverflow.com/questions/8609192/what-is-the-difference-between-null-true-and-blank-true-in-django

no migrations to apply :
https://forum.djangoproject.com/t/no-migrations-to-apply-when-run-migrate-after-makemigrations/15519



location pin on django app:
https://sbabashahi.medium.com/add-location-point-to-django-postgresql-app-803ae4a57d48
https://www.youtube.com/watch?v=2uFJ43DvhHg
https://www.abstractapi.com/guides/django-geolocation

dd summernote:
https://ctrlzblog.com/how-to-add-a-text-editor-to-a-django-blog-with-summernote/

location pin on django app:
https://sbabashahi.medium.com/add-location-point-to-django-postgresql-app-803ae4a57d48
https://www.youtube.com/watch?v=2uFJ43DvhHg
https://www.abstractapi.com/guides/django-geolocation


add summernote:
https://ctrlzblog.com/how-to-add-a-text-editor-to-a-django-blog-with-summernote/

no migrations to apply :
https://forum.djangoproject.com/t/no-migrations-to-apply-when-run-migrate-after-makemigrations/15519

django templates documentation :
https://github.com/Williano/django-bona-blog/blob/master/blog/templates/blog/blog_base.html
https://www.youtube.com/watch?v=_s6g6yP0ahY

over ride css styles with my style.css file 
https://www.google.com/search?q=how+to+make+my+style.css+to+override+bootstrap+and+django&oq=how+to+make+my+style.css+to+override+bootstrap+and+django+&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigATIHCAIQIRigATIHCAMQIRigATIHCAQQIRigAdIBCTIxNjE4ajBqNKgCALACAA&sourceid=chrome&ie=UTF-8


geo location :
https://pypi.org/project/django-easy-maps/
https://developer.mozilla.org/en-US/docs/Web/API/
https://stackoverflow.com/questions/64113710/extracting-gps-coordinates-from-image-using-python
https://thepythoncode.com/article/extracting-image-metadata-in-python

traceback error :
https://realpython.com/python-traceback/#valueerror

send location to my django server:
https://stackoverflow.com/questions/44169448/how-to-send-latitude-and-longitude-to-django-server-using-ajax


crispyform 
https://stackoverflow.com/questions/75495403/django-returns-templatedoesnotexist-when-using-crispy-forms

django eas maps:
https://pypi.org/project/django-easy-maps/


error loading because MIM is not executable :
https://stackoverflow.com/questions/50778910/refused-to-execute-script-from-because-its-mime-type-text-html-is-not-execut


error mim type :
https://stackoverflow.com/questions/48248832/stylesheet-not-loaded-because-of-mime-type/50173968
https://stackoverflow.com/questions/50778910/refused-to-execute-script-from-because-its-mime-type-text-html-is-not-execut
https://stackoverflow.com/questions/48248832/stylesheet-not-loaded-because-of-mime-type/50173968
rendering data on the console :
https://stackoverflow.com/questions/70625340/uncaught-in-promise-typeerror-cannot-read-properties-of-undefined-reading-d\

adressFields:
https://helpv2.quickbase.com/hc/en-us/articles/4570349602836


non nullable fields :
https://ctrlzblog.com/django-migrations-how-to-add-non-nullable-fields-without-compromising-your-database/exit
https://djangopackages.org/packages/p/django-address/

styling icons:
https://stackoverflow.com/questions/50557610/have-two-font-awesome-icons-side-by-side

center raw container:
https://stackoverflow.com/questions/13462535/center-contents-of-bootstrap-row-container

images responsiveness:
https://www.w3schools.com/bootstrap/bootstrap_images.asp#:~:text=Responsive%20images%20automatically%20adjust%20to,nicely%20to%20the%20parent%20element.
https://getbootstrap.com/docs/4.0/components/card/
https://stackoverflow.com/questions/61617160/bootstrap-4-card-image-resizing-on-mobile

null- violation
https://bobbyhadz.com/blog/javascript-cannot-read-property-classlist-of-null
https://stackoverflow.com/questions/48101400/django-null-value-in-column-user-id-violates-not-null-constraint-detail-faili
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-not-null-constraint/
https://www.commandprompt.com/education/how-to-add-or-drop-not-null-constraints-in-postgresql/#:~:text=A%20NOT%20NULL%20constraint%20can,Constraint%20From%20a%20Postgres%20Table%3F

django messages:
https://ordinarycoders.com/blog/article/django-messages-framework


users creating posts:
https://stackoverflow.com/questions/68968059/how-can-i-allow-users-to-create-their-own-posts-in-django
https://stackoverflow.com/questions/68968059/how-can-i-allow-users-to-create-their-own-posts-in-django


importing cloudinary file field to forms :
https://alphacoder.xyz/image-upload-with-django-and-cloudinary/
https://cloudinary.com/documentation/django_image_and_video_upload

https://www.contentstack.com/docs/developers/create-custom-fields/cloudinary#use-your-custom-field
https://alphacoder.xyz/image-upload-with-django-and-cloudinary/
https://stackoverflow.com/questions/59448227/imagefield-object-has-no-attribute-value-from-datadict

default slug value :
https://stackoverflow.com/questions/4884584/django-generate-default-slug

over ride bootstrap properties :
https://www.google.com/search?q=how+to+over+ride+all+the+blue+colors+of+the+bootstrap+theme+in+css&oq=how+to+over+ride+all+the+blue+colors+of+the+bootstrap+theme+&gs_lcrp=EgZjaHJvbWUqCQgDECEYChigATIGCAAQRRg5MgkIARAhGAoYoAEyCQgCECEYChigATIJCAMQIRgKGKABMgkIBBAhGAoYoAHSAQkxOTc4NmowajeoAgCwAgA&sourceid=chrome&ie=UTF-8
https://blog.hubspot.com/website/how-to-override-bootstrap-css#how-to-customize-bootstrap-colors-sass-variables

styling:
https://venngage.com/blog/pastel-color-palettes/

navbar burger links:
https://stackoverflow.com/questions/35233307/add-sidebar-links-to-bootstrap-hamburger-menu
https://getbootstrap.com/docs/4.1/components/navbar/

rendering comments ;
https://stackoverflow.com/questions/67886427/comments-in-the-admin-panel-are-added-but-they-are-not-visible-on-the-site

[Erase Migrations](https://stackoverflow.com/questions/28404461/can-i-delete-the-django-migration-files-inside-migrations-directory)
[Reset Migrations](https://medium.com/@mustahibmajgaonkar/how-to-reset-django-migrations-6787b2a1e723)
[Slug](https://github.com/statamic/v2-hub/issues/1514)
[form validation](https://codereview.stackexchange.com/questions/154820/raise-error-when-slug-already-exists)
[slug](https://stackoverflow.com/questions/56330503/how-to-fix-post-with-this-user-already-exists-error-on-django-while-trying-to)
[Search Function](https://www.youtube.com/watch?v=AGtae4L5BbI)
[Search bar](https://getbootstrap.com/docs/5.2/components/navbar/)
[TypeError](https://www.dhiwise.com/post/troubleshooting-the-cannot-read-properties-of-null-error)
[Django favourites](https://www.youtube.com/watch?v=1XiJvIuvqhs)
[ImageFiled](https://www.geeksforgeeks.org/imagefield-django-models/)
[Cloudinary Imafield](https://cloudinary.com/blog/placeholder_images_and_gravatar_integration_with_cloudinary)
[default](https://www.geeksforgeeks.org/default-django-built-in-field-validation/)
[Searchbar](https://www.youtube.com/watch?v=XIwA6g34jZo&t=453s)
[Modals](https://ux.stackexchange.com/questions/136055/what-is-the-best-way-to-add-edit-and-delete-buttons-to-a-modal)
[Modals](https://symfonycasts.com/screencast/last-stack/modal-edit)
[Modals](https://github.com/MedicOneSystems/livewire-datatables/issues/90)
[Ajax](https://api.jquery.com/jQuery.ajax/)
[Ajax](https://www.geeksforgeeks.org/how-to-make-ajax-call-from-javascript/)
[Fetch()](https://www.geeksforgeeks.org/javascript-fetch-method/)
[Database table generator](https://codebeautify.org/sql-table-generator)
[Navbar](https://stackoverflow.com/questions/46221287/dropdown-link-not-working-in-navigation-bar-bootstrap)
[Image Responsivenes](https://stackoverflow.com/questions/63648620/bootstrap-image-not-displaying-on-smaller-screens)
[Pagination](https://getbootstrap.com/docs/4.0/components/pagination/)
[Pagination](https://design-system.w3.org/components/pagination.html)
[Navbarstyling](https://forum.bootstrapstudio.io/t/how-to-set-the-navbar-to-full-width-of-the-browser/7385)
[Navbar](https://www.w3schools.com/bootstrap/bootstrap_navbar.asp)
[Bootstrap Modal](https://www.w3schools.com/bootstrap/bootstrap_modal.asp)
[Dev Tools](https://stackoverflow.com/questions/67252231/what-is-the-purpose-of-this-purple-dashed-line-area#:~:text=It%20is%20white%20space.,area%20by%20the%20Google%20inspector.)
[Flex](https://stackoverflow.com/questions/36247140/why-dont-flex-items-shrink-past-content-size)
[Flex Container](https://www.tutorialrepublic.com/faq/how-to-set-space-between-flex-items-using-css.php#:~:text=Answer%3A%20Use%20CSS%20justify%2Dcontent,set%20space%20between%20flexbox%20items.)