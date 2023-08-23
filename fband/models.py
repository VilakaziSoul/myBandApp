from django.db import models

class Album(models.Model):
    """
    Model representing an album.
    """
    
    # Fields for the Album model
    
    title = models.CharField(max_length=200)
    """
    The title of the album.
    """
    
    description = models.TextField()
    """
    A description of the album.
    """
    
    cover_image = models.ImageField(
        upload_to='album_covers/',
        default='path_to_default_image.png'
    )
    """
    The cover image of the album.
    
    :param upload_to: The directory to upload cover images.
    :param default: The default cover image path.
    """
    
    def __str__(self):
        """
        Return a string representation of the album.
        """
        return self.title
