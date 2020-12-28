import numpy as np
import discord
import os
from keep_alive import keep_alive

timetable= np.array([
                ["DAY-ORDER",1,2,3,4,5,6],
                ["9:00-10:00","SEMICONDUCTOR","MATHS","ENGLISH","BEEE","PSP","EGD"],
                ["10:00-10:40","MATHS","MATHS","ENGLISH","BEEE","PSP","EGD"],
                ["11:00-12:00","COI","SEMICONDUCTOR","MATHS","ENGLISH","BEEE","PSP"],
                ["13:00-14:00","EGD","EGD","BEEE","SEMICONDUCTOR","MATHS","ENGLISH"],
                ["14:00-14:30","SEMICONDUCTOR_LAB","EGD_LAB","BEEE_LAB","YOGA","OVER","OVER"],
                ["14:30-15:30","SEMICONDUCTOR_LAB","EGD_LAB","BEEE_LAB","YOGA","OVER","OVER"]]).T


day1=timetable[0:2:1,1:].T
day2=timetable[0:3:2,1:].T
day3=timetable[0:4:3,1:].T
day4=timetable[0:5:4,1:].T
day5=timetable[0:6:5,1:].T
day6=timetable[0:7:6,1:].T
day7=timetable[0:8:7,1:].T


help= """Type "day1","day2" or "day4" with respect to the current day order.This bot is still UNDER CONSTRUCTION so For suggestions Contact @admins/@arpan/@deepak"""


client=discord.Client()



@client.event
async def on_ready():
  print('Under Construction by {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('day1'):
    await message.channel.send(day1)
  
  if message.content.startswith('day2'):
    await message.channel.send(day2)

  if message.content.startswith('day3'):
    await message.channel.send(day3)

  if message.content.startswith('day4'):
    await message.channel.send(day4)

  if message.content.startswith('day5'):
    await message.channel.send(day5)

  if message.content.startswith('day6'):
    await message.channel.send(day6)
  
  if message.content.startswith('day-order'):
    await message.channel.send(timetable)

  if message.content.startswith('help'):
    await message.channel.send(help)



keep_alive()
client.run(os.getenv('TOKEN'))
 

