import os
from PIL import Image, ImageDraw

class SimpleSpriteHandler:
    """A simplified sprite handler that uses PIL instead of pygame"""
    
    def __init__(self):
        """Initialize the sprite handler"""
        self.colors = {
            'cow': (139, 69, 19),  # Brown
            'buffalo': (50, 50, 50),  # Dark gray
            'goat': (200, 200, 200),  # Light gray
            'sheep': (255, 255, 255)  # White
        }
    
    def create_sprite(self, breed_name, size=(200, 150)):
        """Create a simple sprite for the given breed"""
        # Determine color based on breed
        color = self._get_color_for_breed(breed_name)
        
        # Create a new image with white background
        image = Image.new('RGB', size, (255, 255, 255))
        draw = ImageDraw.Draw(image)
        
        # Draw a simple animal shape
        # Body (ellipse)
        draw.ellipse([(20, 30), (size[0]-40, size[1]-30)], fill=color)
        
        # Head (circle)
        head_size = min(size) // 3
        draw.ellipse([(size[0]-head_size-30, 20), 
                      (size[0]-30, 20+head_size)], fill=color)
        
        # Legs (rectangles)
        leg_width = size[0] // 20
        leg_height = size[1] // 3
        leg_positions = [
            (size[0]//4, size[1]-leg_height),
            (size[0]//4 + size[0]//6, size[1]-leg_height),
            (size[0]//2 + size[0]//12, size[1]-leg_height),
            (size[0]//2 + size[0]//4, size[1]-leg_height)
        ]
        
        for pos in leg_positions:
            draw.rectangle([pos, (pos[0]+leg_width, pos[1]+leg_height-10)], 
                          fill=(color[0]-20, color[1]-20, color[2]-20))
        
        return image
    
    def _get_color_for_breed(self, breed_name):
        """Get appropriate color for the breed"""
        breed_lower = breed_name.lower()
        
        for key, color in self.colors.items():
            if key in breed_lower:
                return color
        
        # Default to cow color
        return self.colors['cow']
    
    def save_sprite_image(self, breed_name, output_path):
        """Create and save a sprite for the given breed"""
        sprite = self.create_sprite(breed_name)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        sprite.save(output_path)
        return output_path