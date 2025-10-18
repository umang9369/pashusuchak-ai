import os
import random
from simple_sprite_handler import SimpleSpriteHandler

def test_mcp_sprites():
    """Generate test sprites for all breeds using the simple sprite handler"""
    print("Starting MCP testsprite generation...")
    
    # Initialize the sprite handler
    handler = SimpleSpriteHandler()
    
    # Create output directory
    output_dir = os.path.join(os.path.dirname(__file__), 'test_sprites')
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate sprites for different breeds
    breeds = ["Holstein Cow", "Murrah Buffalo", "Gir Cow", "Sahiwal Cow"]
    results = []
    
    for breed in breeds:
        print(f"Generating sprite for {breed}...")
        
        # Create output path
        sprite_filename = f"mcp_{breed.replace(' ', '_')}.png"
        sprite_path = os.path.join(output_dir, sprite_filename)
        
        try:
            # Generate and save sprite
            handler.save_sprite_image(breed, sprite_path)
            
            # Add to results
            results.append({
                "breed": breed,
                "confidence": round(random.uniform(0.8, 0.95), 2),
                "sprite_path": sprite_path
            })
            
            print(f"✓ Successfully generated sprite for {breed} at {sprite_path}")
        except Exception as e:
            print(f"✗ Error generating sprite for {breed}: {e}")
    
    print("\nMCP testsprite generation complete!")
    print(f"Generated {len(results)} sprites in {output_dir}")
    
    return results

if __name__ == "__main__":
    test_mcp_sprites()