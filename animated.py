import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Animated Graphs")

##### Life Expectancy #####
###########################

df = px.data.gapminder() #I think this is example data that comes with plotly

st.write("## Life Expectancy")
st.write("This is data made famous by Hans Rosling.")

#st.write(df.head(4)) #Uncomment this if you want to show the data

fig = px.scatter(df,x="gdpPercap",y="lifeExp",
size="pop",color="continent",hover_name="country",
log_x=True,size_max=55,range_x=[100,100000],range_y=[25,90],
animation_frame="year",animation_group="country")
fig.update_layout(width=800)
st.write(fig)

##### COVID Data #####
######################

st.title("Daily COVID Cases")

covid = pd.read_csv('https://raw.githubusercontent.com/shinokada/covid-19-stats/master/data/daily-new-confirmed-cases-of-covid-19-tests-per-case.csv')
covid.columns = ['Country','Code','Date','Confirmed','Days since confirmed']
covid['Date'] = pd.to_datetime(covid['Date']).dt.strftime('%Y-%m-%d')

country_options = covid['Country'].unique().tolist()
country = st.multiselect('Choose countries',country_options,['Brazil','China','United States'])
covid = covid[covid['Country'].isin(country)]


fig2 = px.bar(covid,x="Country", y="Confirmed",color="Country",
range_y = [0,35000],animation_frame="Date",animation_group="Country")

fig2.layout.updatemenus[0].buttons[0].args[1]['frame']['duration']=30
fig2.layout.updatemenus[0].buttons[0].args[1]['transition']['duration']=5


fig2.update_layout(width=800)
st.write(fig2)
