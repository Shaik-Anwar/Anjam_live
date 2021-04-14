from django.db import models

class project(models.Model):
    BRANCH1= (
            ('ECE', 'ECE'),
            ('EEE', 'EEE'),
            ('CSE', 'CSE'),
            ('IT', 'IT'),
            ('MEC', 'MEC'),
            )


    BRANCH2= (
            ('ECE', 'ECE'),
            ('EEE', 'EEE'),
            ('CSE', 'CSE'),
            ('IT', 'IT'),
            ('MEC', 'MEC'),
            )

    BRANCH3= (
            ('ECE', 'ECE'),
            ('EEE', 'EEE'),
            ('CSE', 'CSE'),
            ('IT', 'IT'),
            ('MEC', 'MEC'),
            )
       
    PLATFORM1 = (
        ('EMBEDDED SYSTEM', 'EMBEDDED SYSTEM'),
        ('VLSI', 'VLSI'),
        ('IOT', 'IOT'),
        ('WEB TECHNOLOGY', 'WEB TECHNOLOGY'),
        ('IMAGE PROCESSING', 'IMAGE PROCESSING'),
        ('ROBOTICS', 'ROBOTICS'),
        ('POWER ELECTRONICS', 'POWER ELECTRONIC'),
        ('DATA SCIENCE', 'DATA SCIENCE'),
        ('CLOUD COMPUTING', 'CLOUD COMPUTING'),
        ('ELECTRONICS', 'ELECTRONICS'),
        ('COMMUNICATION', 'COMMUNICATION'),
        ('COMPUTER VISION', 'COMPUTER VISION'),
        ('DEEP LEARNING', 'DEEP LEARNING'),
    )
    
    PLATFORM2 = (
        ('EMBEDDED SYSTEM', 'EMBEDDED SYSTEM'),
        ('VLSI', 'VLSI'),
        ('IOT', 'IOT'),
        ('WEB TECHNOLOGY', 'WEB TECHNOLOGY'),
        ('IMAGE PROCESSING', 'IMAGE PROCESSING'),
        ('ROBOTICS', 'ROBOTICS'),
        ('POWER ELECTRONICS', 'POWER ELECTRONIC'),
        ('DATA SCIENCE', 'DATA SCIENCE'),
        ('CLOUD COMPUTING', 'CLOUD COMPUTING'),
        ('ELECTRONICS', 'ELECTRONICS'),
        ('COMMUNICATION', 'COMMUNICATION'),
        ('COMPUTER VISION', 'COMPUTER VISION'),
        ('DEEP LEARNING', 'DEEP LEARNING'),
    )
    PLATFORM3 = (
        ('EMBEDDED SYSTEM', 'EMBEDDED SYSTEM'),
        ('VLSI', 'VLSI'),
        ('IOT', 'IOT'),
        ('WEB TECHNOLOGY', 'WEB TECHNOLOGY'),
        ('IMAGE PROCESSING', 'IMAGE PROCESSING'),
        ('ROBOTICS', 'ROBOTICS'),
        ('POWER ELECTRONICS', 'POWER ELECTRONIC'),
        ('DATA SCIENCE', 'DATA SCIENCE'),
        ('CLOUD COMPUTING', 'CLOUD COMPUTING'),
        ('ELECTRONICS', 'ELECTRONICS'),
        ('COMMUNICATION', 'COMMUNICATION'),
        ('COMPUTER VISION', 'COMPUTER VISION'),
        ('DEEP LEARNING', 'DEEP LEARNING'),
    )
 
    title = models.CharField(max_length=255, null=True)
    project_id = models.CharField(max_length=200, null=True)
    branch1 = models.CharField(max_length=200, null=True, choices=BRANCH1)
    branch2 = models.CharField(max_length=200, null=True, choices=BRANCH2, blank = True)
    branch3 = models.CharField(max_length=200, null=True, choices=BRANCH3, blank = True)
    platform1 = models.CharField(max_length=200, null=True, choices=PLATFORM1)
    platform2 = models.CharField(max_length=200, null=True, choices=PLATFORM2, blank = True)
    platform3 = models.CharField(max_length=200, null=True, choices=PLATFORM3, blank = True)
    upload = models.FileField(upload_to='uploads/', max_length=100, blank = True)

    def __str__(self):
        return self.title
