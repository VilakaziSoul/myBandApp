from django.db import models

class Album(models.Model):
    # Fields for the Album model
    title = models.CharField(max_length=200)       # Title of the album
    description = models.TextField()               # Description of the album
    cover_image = models.ImageField(
        upload_to='album_covers/',                 # Directory to upload cover images
        default=r'C:/Users/Sidwe/OneDrive/Documents/HyperionDev/Level 2/L2T23/myBand/static/images'
        )                                           # Default cover image path

    def __str__(self):
        return self.title   # String representation of the album object
