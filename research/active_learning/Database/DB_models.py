'''
DB_models.py

Defines model classes representing database tables used in active learning for classification.

'''

from peewee import *


db_proxy = Proxy() # create a proxy backend for the database


class Info(Model):
    '''
    Table containing information about the target dataset.
    '''
    name = CharField() # name of dataset
    description = CharField()
    contributor = CharField()
    version = IntegerField()
    year = IntegerField()
    date_created = DateField()
    RM = FloatField(null = True, default= -1) # mean in RGB channels(?)
    GM = FloatField(null = True, default= -1)
    BM = FloatField(null = True, default= -1)
    RS = FloatField(null = True, default= -1) # standard deviation in RGB channels (?)
    GS = FloatField(null = True, default= -1)
    BS = FloatField(null = True, default= -1)

    class Meta:
        database = db_proxy


class Image(Model):
    '''
    Table containing information about each image in the target dataset.
    '''
    id = CharField(primary_key=True)
    file_name = CharField()
    #label= CharField()
    width = IntegerField(null = True) # image dimensions in pixels
    height = IntegerField(null= True)
    location = CharField(null = True) # location of camera trap
    datetime = DateTimeField(null = True)
    seq_id = CharField(null= True) # sequence identifier
    seq_num_frames = IntegerField(null = True) # number of frames in sequence
    frame_num = IntegerField(null = True) # which frame number in sequence
    
    class Meta:
        database = db_proxy