#!/usr/bin/env python
# coding: utf-8

# ## Project: Personal Webpage
# 
# #### Author: Elom Kwamin, FRM
# 
# #### Date: 5.01.2024

# ### step 1: import required packages 

# In[1]:


# packages for front end
from jupyter_dash import JupyterDash
from dash import Dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate
from dash import dash_table
import dash_extensions as de


# In[2]:


# lotties json
hello_lottie_url = "https://lottie.host/c57a06dc-0bbc-4f22-b345-3c0115030ea9/G0GQpemRva.json"
analyst_lottie_url = "https://lottie.host/8d1aa277-f7af-4087-ab07-4e6a6632791a/oaW50SV1n4.json"

linkedin_lottie_url = "https://lottie.host/c57a06dc-0bbc-4f22-b345-3c0115030ea9/G0GQpemRva.json"
youtube_lottie_url = "https://lottie.host/8d1aa277-f7af-4087-ab07-4e6a6632791a/oaW50SV1n4.json"
instagram_lottie_url = "https://lottie.host/d9fb345b-ef36-474b-ae20-91e762682f60/e4UvyiK7NB.json"
gmail_lottie_url = "https://lottie.host/be5e90ad-1f51-4e23-a9b6-495d7b75e337/HedBu0QYP8.json"

lotties_options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))


# In[ ]:





# ### step 2: instantiate app

# In[3]:


app = Dash(__name__,
           external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP],
          meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1,'}])

# Set the title of the app
app.title = 'Elom Kwamin, FRM'

server = app.server # required line before upload to render


# In[ ]:





# ### step 3: app layout

# #### 3.0 layout for web app header

# In[4]:


header_section = html.Div([
        
        html.H1("Elom Tettey Kwamin, FRM", className="text-left mt-2 mb-1", style={'font-family': 'Broadway, sans-serif'}),
        
        html.H5(" Structured Finance Analyst | Data Analyst ",className="text-left mb-0", style={'font-family': 'Calibri Light'}),
        
        html.Div(style={"border-bottom": "10px groove white", "padding": "5px", }), 
    ], 
        
    style={"border": "0px royal blue",  # 2px border with black color
                        'box-shadow': '12px 12px 12px 12px rgba(0, 0, 0, 0.2)',
                        "padding": "10px"  },
         
    className="header")


# #### 3.1 layout for social platform

# In[5]:


# Create references with a fixed footer style
socials_section = dbc.Row([
    html.Div([
        html.A(html.I(className="bi bi-youtube text-danger text-center", style={'font-size': '20px', 'margin': '10px'}),
               href="https://www.youtube.com/@DatawithElom", 
               target="_blank",
        ),
        
        html.A(html.I(className="bi bi-instagram text-danger text-center", style={'font-size': '20px', 'margin': '10px'}),
               href="http://instagram.com/data.with.elom",
               target="_blank", 
        ),
        
        html.A(html.I(className="bi bi-linkedin text-primary text-center", style={'font-size': '20px', 'margin': '10px'}),
               href="http://linkedin.com/in/elom-tettey-kwamin-frm®-53029468",
               target="_blank", 
        ),
           
    ], style={"display": "flex", "justify-content": "center", "align-items": "center"}), 

], 
justify='center')


# #### 3.2 layout for profile

# In[6]:


# First page layout with introduction and profile picture

profile_section =  dbc.Row([
        # Introduction column
        dbc.Col([
            
            html.Div([
            
            html.H2("About Me", className="mt-4 mb-4", style={'font-family': 'Broadway, sans-serif'}),
            html.P("Hello, I'm Elom Tettey Kwamin, a dedicated quantitative analyst with a passion for leveraging data and analytics to drive insights in the world of finance. I hold a Master's degree in Quantitative Finance and Economics, and my professional journey has led me to specialize in credit risk assessment and pricing financial products.", style={'font-size': '18px', 'font-family': 'Calibri Light'}),
            html.H3("Key Expertise", style={'font-family': 'Broadway, sans-serif'}),
            html.Ul([
                html.Li([html.Strong("Quantitative Finance:"), " I bring a strong foundation in quantitative finance, ensuring a robust understanding of complex financial instruments and risk management strategies."], 
                        style={'font-size': '18px', 'font-family': 'Calibri Light'}),
                html.Li([html.Strong("Data Analysis and Analytics:")," My enthusiasm for data analysis is evident in my work. I enjoy exploring datasets, extracting meaningful information, and deriving actionable insights to inform strategic decision-making."]
                        , style={'font-size': '18px', 'font-family': 'Calibri Light'}),
                html.Li([html.Strong("Machine Learning in Finance:")," I thrive on exploring the intersection of finance and technology. I actively apply machine learning techniques to enhance financial modeling, risk assessment, and decision-making processes."]
                        , style={'font-size': '18px', 'font-family': 'Calibri Light'}),
                html.Li([html.Strong("Tool Development:"), " I take pleasure in developing tools that streamline workflows and enhance efficiency. Proficient in Python and VBA, I create solutions that empower teams to achieve their goals with greater precision."]
                        , style={'font-size': '18px', 'font-family': 'Calibri Light'}),
            ]),
#             html.H3("What Drives Me"),
#             html.P("I am driven by the dynamic nature of finance and the transformative power of data. My goal is to contribute to the evolution of the financial landscape by embracing innovation, continuous learning, and the application of cutting-edge technologies."),
#             html.H3("Let's Connect"),
#             html.P("I'm excited to share my experiences, insights, and projects with you. Explore my personal web page to discover more about my professional journey and the exciting projects I've been involved in. Feel free to connect, and let's explore the possibilities at the intersection of finance and technology."),
            ], style={
                "border": "0px ridge white",
                "box-shadow": "12px 12px 12px 12px rgba(0, 0, 0, 0.2)",
                "padding": "5px",
            }),
            
            ], width=4, xs=12, sm=12, lg={'size':4, 'offset':0}),

        # Profile picture column
        dbc.Col([
            html.Div([
                dbc.CardImg(
                    src="assets/elom_kwamin_profile_pic.jpeg",  
                    className='rounded-center',
                    style={
                        "maxWidth": "100%",
                        "height": "100%",
                        "object-fit": "contain",
                        "opacity": 0.9,
                    },
                ),
            ], style={
                "border": "0px ridge white",
                "box-shadow": "12px 12px 12px 12px rgba(0, 0, 0, 0.2)",
                "padding": "10px",
                "height": "650px",
            }),
            
        ], width=4, xs=12, sm=12, lg={'size':4, 'offset':0}),

    ], justify='center', style={ "paddingTop": "150px", "paddingBottom": "150px"}) 


# #### 3.3 layout for projects and resume

# In[7]:


# build table for projects tab content
table_header = [html.Thead([html.Tr([html.Th("Project name"), html.Th("Links")])],style={'background-color': 'black', 'color': 'white'})]

row1 = html.Tr([html.Td("Loan Book Visualizer: Automate analysis of a bank loan book with Python and Dash"), 
                html.Td(html.A("Link 1", target="_blank", href="https://loan-book-visualizer-app.onrender.com"))])

row2 = html.Tr([html.Td("Macro Data Explorer: Create a dashboard from macro data for analysis"), 
                html.Td(html.A("Link 2", target="_blank", href="https://macro-data-explorer-app.onrender.com"))])


table_body = [html.Tbody([row1, row2],style={'background-color': 'black', 'color': 'white'})]
# table_body = [html.Tbody([row1, row2, row3, row4])]

table = dbc.Table(table_header + table_body, bordered=True, style={'background-color': 'black', 'color': 'white'})

# Define the content for each tab

# project tab content
tab_projects_content = dbc.Card(
    html.Div([
        table        
    ],style={'background-color': 'black', 'color': 'white'})
)

# resume tab content
tab_resume_content = dbc.Card( 
    html.Div([
    dbc.CardBody([
        
        dbc.Row([
            
                dbc.Button(id='download-cv-button', 
                           n_clicks=0, outline=True, 
                           children = [html.I(className="fa fa-cloud-download mr-1"), "Download CV"],
                           color='primary',
                           className='button',
                           style={'width': '140px', 'margin-left': 'auto'}
                    ),
                
            ], justify='end', className='mt-1'),
            
           
            
            html.Br(),
        
            dbc.Row([
                html.Div([
                dbc.Col([
                dbc.CardImg(src="assets/passport_pic.jpeg", className='rounded-center"', 
                            style={"maxWidth": 180, "opacity": 0.8, "objectFit": "cover"},), 
                ],lg={'size':2, 'offset':0}, sm=12, className='text-left'),
                ],style={"display": "flex", "justify-content": "center", "align-items": "center"}),
#                 dbc.Col([
                
#                 html.A('I am a results-oriented finance analyst holding a dual Master degrees in Quantitative Finance '), 
#                 html.A('and Quantitative Economics from the University of Kiel.'),
#                 html.A(' I hold the esteemed FRM designation and have a strong passion for data analysis and machine learning.'),
#                 html.A(' I am adept at harnessing the power of data analysis and machine learning to drive informed decisions'),
#                 html.A(' and deliver exceptional outcomes.'),
#                 ], lg={'size':8, 'offset':0}, sm=12, className='text-left'),    

            ],justify='center'),
        
             dbc.Row([
                    html.Div([
                        dbc.Col([
                        html.I(className="bi bi-linkedin me-3 text-primary text-center"),
                        html.A("Elom Kwamin, FRM", 
                               href="http://linkedin.com/in/elom-tettey-kwamin-frm®-53029468",
                               target="_blank", 
                               style={'text-decoration':'none'},
                              ),
                        ],lg={'size':2, 'offset':0}, sm=12, className='text-left'),
                    ],style={"display": "flex", "justify-content": "center", "align-items": "center"}),
                ]),


            html.Br(),
            html.Br(),
            
            html.I(className="bi bi-building  me-2 text-primary text-center"),
            html.A('Work Experience'),
        
            html.Hr(),
            html.Ul([           
                html.Li('June 2022 - Current: Specialist, Structured Finance - Scope Ratings GmbH'),
                html.Li('Dec 2020 - May 2022: Associate Analyst, Structured Finance - Scope Ratings GmbH'),
                html.Li('Mar 2018 - Apr 2019: Quantitative Analyst - TTMzero'),
            ]),
            
            html.Br(),
            html.Br(),
        
            html.I(className="bi bi-book me-2 text-primary text-center"),
            html.A('Education'),
        
            html.Hr(),
            html.Ul([           
                html.Li('2015 - 2017: MSc. Quantitative Economics, University of Kiel'),
                html.Li('2013 - 2016: MSc. Quantitative Finance, University of Kiel'),
                html.Li('2008 - 2012: BSc. Actuarial Science, Kwame Nkrumah University of Science & Technology'),
            ]),
            
            html.Br(),
            html.Br(),
        
   
            html.I(className="bi bi-tools me-2 text-primary text-center"),
            html.A('Skills', style={'font':'bold'}),
          
        
            html.Hr(),
            html.Ul([
                html.Li('Machine Learning'),
                html.Li('Data analysis & analytics'),
                html.Li('VBA'),
                html.Li('Tool development in Python'),
            ]),
              
        ],style={"border": "0px ridge silver",  # outset, groove
                  'box-shadow': '10px 10px 10px 10px rgba(0, 0, 0, 0.2)',
                  "padding": "10px"  } # Add padding for spacing}
    ),
    ],style={'background-color': 'black', 'color': 'white'}),
className="mt-4 w-80 border-0 bg-transparent",)



# Create the tabs
tabs = dbc.Tabs([
        dbc.Tab(tab_projects_content, label="Projects", className="mt-10", activeTabClassName="fw-bold fst-italic"),
        dbc.Tab(tab_resume_content, label="Resume", className="mt-10", activeTabClassName="fw-bold fst-italic"), 
    ])


# In[8]:


# layout of tabs
tabs_section = html.Div([   
    dbc.Row([
        dbc.Col([tabs], lg={'size':8, 'offset':2}, sm=12),
    ]),
    
    dcc.Download(id='download-cv-component'),
 
], style={'background-color': 'black', 'color': 'white'})


# #### 3.4 final layout

# In[9]:


app.layout = dbc.Container([
    
    header_section,
    
    profile_section,
    
    tabs_section,  
    
    html.Br(),
    
    socials_section,
    
    html.Br(),
    
], fluid=True, style={'background-color': 'black', 'color': 'white', "min-height": "100vh"})

# # Set background color for the body
# app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})


# In[ ]:





# ### step 4: callbacks 

# In[10]:


# callback for downloading resume
@app.callback(
    Output('download-cv-component', 'data'),
    Input('download-cv-button', 'n_clicks'),
    prevent_initial_call = True,
)

def download_resume(n_clicks):

    return dcc.send_file('./assets/elom_kwamin_resume.pdf')


# ### step 5: run app

# In[11]:


if __name__ == '__main__':
    app.run_server(debug=False)


# In[ ]:





# In[ ]:




