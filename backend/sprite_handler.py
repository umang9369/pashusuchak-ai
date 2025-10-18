import pygame
import os

class SpriteHandler:
    def __init__(self):
        """Initialize the sprite handler for animal visualization"""
        pygame.init()
        self.sprites = {}
        self.load_sprites()
        
    def load_sprites(self):
        """Load all animal sprites from the sprites directory"""
        sprite_dir = os.path.join(os.path.dirname(__file__), '..', 'public', 'sprites')
        os.makedirs(sprite_dir, exist_ok=True)
        
        # Default sprites if no images are available
        self.sprites = {
            'cow': self._create_default_sprite((200, 150), (139, 69, 19)),  # Brown
            'buffalo': self._create_default_sprite((220, 160), (50, 50, 50)),  # Dark gray
            'goat': self._create_default_sprite((180, 130), (200, 200, 200)),  # Light gray
            'sheep': self._create_default_sprite((190, 140), (255, 255, 255))   # White
        }
        
    def _create_default_sprite(self, size, color):
        """Create a default sprite surface with given size and color"""
        surface = pygame.Surface(size, pygame.SRCALPHA)
        
        # Draw a simple animal shape
        pygame.draw.ellipse(surface, color, (0, 0, size[0], size[1]))
        pygame.draw.ellipse(surface, (color[0]-20, color[1]-20, color[2]-20), 
                           (size[0]*0.7, 0, size[0]*0.3, size[1]*0.3))  # Head
        
        # Add legs
        leg_color = (color[0]-30, color[1]-30, color[2]-30)
        leg_width = size[0] * 0.1
        leg_height = size[1] * 0.4
        
        # Four legs
        for i in range(4):
            x_pos = size[0] * (0.2 + (i % 2) * 0.5)
            y_pos = size[1] * (0.6 + (i // 2) * 0.1)
            pygame.draw.rect(surface, leg_color, (x_pos, y_pos, leg_width, leg_height))
        
        return surface
    
    def get_sprite(self, breed_name):
        """Get sprite for a specific breed"""
        breed_lower = breed_name.lower()
        
        # Match the breed to available sprites
        for key in self.sprites:
            if key in breed_lower:
                return self.sprites[key]
        
        # Return default cow sprite if no match
        return self.sprites['cow']
    
    def save_sprite_image(self, breed_name, output_path):
        """Save the sprite as an image file"""
        sprite = self.get_sprite(breed_name)
        pygame.image.save(sprite, output_path)
        return output_path

# Test function
def test_sprite():
    """Test function to generate and display a sprite"""
    handler = SpriteHandler()
    
    # Create test directory
    test_dir = os.path.join(os.path.dirname(__file__), 'test_sprites')
    os.makedirs(test_dir, exist_ok=True)
    
    # Generate and save test sprites
    breeds = ['Holstein Cow', 'Murrah Buffalo', 'Gir Cow', 'Sahiwal Cow']
    paths = []
    
    for breed in breeds:
        output_path = os.path.join(test_dir, f"{breed.replace(' ', '_')}.png")
        handler.save_sprite_image(breed, output_path)
        paths.append(output_path)
    
    return paths

if __name__ == "__main__":
    # Run test when script is executed directly
    test_paths = test_sprite()
    print(f"Test sprites generated at: {test_paths}")