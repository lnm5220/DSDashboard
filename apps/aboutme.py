import dash_bootstrap_components as dbc
import dash_html_components as html

tab1_content = dbc.Card([
    dbc.Row(
            [
                dbc.Col(dbc.CardImg(src="/assets/meTED.jpg", top=True),width=4),
                dbc.Col(dbc.CardImg(src="/assets/cropped.jpg", top=True), width=3),
                dbc.Col(dbc.CardImg(src="/assets/dancers.jpg", top=True), width=4),
            ], justify= "center"
        ),
    dbc.CardBody(
        [
            html.H3("About Me", className="card-text"),
            html.P("Hi! My name is Leah Miller and I am the Data Sciences student who created this dashboard. I am currently a senior in the college of IST\
                and I study Data Sciences with a minor in Bioethics and Medical Humanities. I wanted to create this dashboard to not only show the wide breadth\
                of careers in data sciences but I also wanted to show the process of turning data into something meaningful."),
            html.P("    Data Visualization is only one of the crucial skills that are integral to being a great data scientist. I have always enjoyed learning about data visualization but my true passion\
                emerged during my Summer internship with Eli Lilly, a pharmaceutical company. During my time at Lilly I was able to use the skills I learned\
                in IST to visualize clinical trial data. The meaning behind my work had never been so clear and I was so thankful to have the technical and soft skills\
                needed to succeed at Eli Lilly."),
            html.P("    You may be thinking that creating dashboards, interning at pharmaceutical companies, and loving data visualization is not for you and that's okay!\
                I entered this major not knowing where I would end up and that is the beauty of data sciences! It is a dynamic field with so many options.\
                Not only are there different sectors to work in but there are so many facets to data science like data visualization, machine learning, or data integration\
                to name a few. It is all about finding what YOU are passionate about!"),
            html.P("    The good news is that the College of IST is here to help you explore those passions and find what fits you best. They also offer support to help you find that\
                summer internship where you find your true passion. Take some time to explore this dashboard and see just one example of taking data and turning it into something useful! If you want to learn more about this\
                how I completed thi project, click the About This Project tab above.")
        ]
    )],
    className="mt-3")

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.H3("About This Project", className="card-text"),
            html.P("Hey there! Let's take some time to learn more about the why and how of this dashboard! I'll walk through the process by following the Data Visualization\
                Process which is the general cycle for visualizing data. This cycle will change depending on the kind of data science proejct you are completing!"),
            html.H6("Data Collection"),
            html.P("To begin, let's take a look below at the data we began with."),
            html.Img(src="/assets/othersmalldata.png"),
            html.P("Not too pretty right? This data is in CSV format and is thousands of lines long. I found this data on Kaggle.com and was originally scraped from Glass Door. Kaggle is a great data science resource with lots of open source data to play around with\
                and even projects to compete in! While many people choose to collect their own data through web scraping or surveys, using open source data is a great\
                option for beginners!"),
            html.H6("Data Cleaning"),
            html.P("Although this data is very interesting, it's format is not convenient or usable for someone wanting to explore careers\
                in data sciences. Before the data gets fed to our dashboard, we must clean the data. I used Python to do some simple cleaning like dropping unwanted columns\
                and adding a new column called average salary. This step is important so that the data is ready to be visualized!"),
            html.H6("Visualize"),
            html.P("With clean data, I was able to begin visualizing data science careers on my dashboard. This dashboard is creating using Python, HTML, and DASH- a great tool\
                that can be used with Python. With all of these tools I was able to use the data to show different aspects of the careers like distribution of the sectors,\
                location of the jobs, and average salary. The data went from being a long file that was difficult to read, to a dashboard that allows users to explore the data \
                and take away key points."),
            html.H6("Deploy"),
            html.P("This is the last step and the step that is allowing you to view this dashboard right now! I used Heroku, a free platform for deploying web apps, to host this \
                dashboard for anyone to see. This step varies depending on who you have created your visualization for. Sometimes you might be sending an visualization in an email \
                and other times you may be deploying it on a web app like this!"),
            html.P("This is the behind the scenes of this data science dashboard. These are all skills I learned as a Data Science student in the \
                College of IST!"),
            html.A("Check out the dataset I used.", href='https://www.kaggle.com/rkb0023/glassdoor-data-science-jobs'),
            html.P(""),
            html.A("Check out other dashboards created with Dash.", href='https://dash-gallery.plotly.host/Portal/'),
            html.P(""),
            html.P("Coordinates data courtesy of https://simplemaps.com/data/us-cities")
        ]
    ),
    className="mt-3",
)


layout = dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="About Me"),
        dbc.Tab(tab2_content, label="About This Project")
    ]
)