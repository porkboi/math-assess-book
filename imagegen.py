# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 17:28:08 2023

@author: chris
"""

from PIL import Image

clockface = Image.open("src/clockface.png")
minutehand = Image.open("src/minutehand.png")
minutehand = minutehand.convert("RGBA")
hourhand = Image.open("src/hourhand.png")
hourhand = hourhand.convert("RGBA")

def coinmosiac(coin_image, coinint, vertical=False):
    top = coinint // 3
    bottom = coinint % 3
    
    width, height = coin_image.width, coin_image.height
    ###    
    tiled_size2 = width * 3, height
    tiled_img2 = Image.new(coin_image.mode, tiled_size2, color = (255,255,255))
    row2 , col2 = 0,0
    count2 = 0
    end2 = bottom
    while count2 in range(end2):
        tiled_img2.paste(coin_image, (row2,col2))
        row2 += width
        count2 += 1

    
    #width, height = coin_image.width, coin_image.height
    ###
    tiled_size = width *3, height*3
    tiled_img = Image.new(coin_image.mode, tiled_size, color=(255,255,255))
    row , col = 0,0
    count = 0
    end = 3*top
    while count in range(end):
        tiled_img.paste(coin_image, (row,col))
        if row == 2*width:
            col = height
            row = -width
            row += width
        else:
            row += width
        count += 1
    
    tiled_img.paste(tiled_img2, (0,height*top-1))
    return tiled_img
    
def big_mosiac(*images, vertical=False):
    width, height = images[0].width, images[0].height
    if len(images)==4:
        tiled_size = width*2, height*2
    else:
        tiled_size = width*2, height*1
    tiled_img = Image.new(images[0].mode, tiled_size, color=(255,255,255))
    row , col = 0,0
    for image in images:
        tiled_img.paste(image, (row, col))
        if row == width:
            col = height
            row = -width
            row += width
        else:
            row += width
    return tiled_img

def clockgen(hour, minute):
    minutehand_angle = minute/60*360
    hourhand_angle = hour/12*360 + minute/60*30
    rotated_hourhand = hourhand.rotate(-hourhand_angle)
    rotated_minutehand = minutehand.rotate(-minutehand_angle)
    width, height = clockface.width, clockface.height
    clock_img = Image.new(clockface.mode, (width,height), color=(255,255,255))
    clock_img.paste(clockface, (0,0))
    clock_img.paste(rotated_hourhand, (0,0), rotated_hourhand)
    clock_img.paste(rotated_minutehand, (0,0), rotated_minutehand)
    return clock_img