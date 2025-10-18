// PashuSuchak AI - Main Application JavaScript

document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements
    const imageUpload = document.getElementById('image-upload');
    const uploadBtn = document.getElementById('upload-btn');
    const previewContainer = document.getElementById('preview-container');
    const resultsContainer = document.getElementById('results-container');
    
    // Event Listeners
    imageUpload.addEventListener('change', handleImagePreview);
    uploadBtn.addEventListener('click', analyzeImage);
    
    // Functions
    function handleImagePreview(event) {
        const file = event.target.files[0];
        if (!file) return;
        
        // Clear previous preview
        previewContainer.innerHTML = '';
        
        // Create image preview
        const img = document.createElement('img');
        img.src = URL.createObjectURL(file);
        img.alt = 'Preview Image';
        previewContainer.appendChild(img);
        
        // Reset results
        resultsContainer.innerHTML = '<p>Click "Analyze Breed" to process the image</p>';
    }
    
    async function analyzeImage() {
        const file = imageUpload.files[0];
        if (!file) {
            alert('Please select an image first');
            return;
        }
        
        // Show loading state
        resultsContainer.innerHTML = '<p>Analyzing image... Please wait</p>';
        
        try {
            // Create form data for API request
            const formData = new FormData();
            formData.append('image', file);
            
            // Send to backend API
            const response = await fetch('http://127.0.0.1:5000/api/analyze', {
                method: 'POST',
                body: formData
            });
            
            if (!response.ok) {
                throw new Error('Analysis failed');
            }
            
            const data = await response.json();
            displayResults(data);
            
        } catch (error) {
            resultsContainer.innerHTML = `<p class="error">Error: ${error.message}</p>`;
        }
    }
    
    function displayResults(data) {
        // Clear previous results
        resultsContainer.innerHTML = '';
        
        // Create results HTML
        let resultsHTML = `
            <div class="results-card">
                <h3>Breed Identification Results</h3>
                <div class="breed-result">
                    <p class="breed-name">Detected Breed: <strong>${data.breed}</strong></p>
                    <p class="confidence">Confidence: ${(data.confidence * 100).toFixed(2)}%</p>
                </div>
                <div class="breed-info">
                    <h4>Breed Information:</h4>
                    <p>${data.description}</p>
                </div>
        `;
        
        // Add sprite image if available
        if (data.sprite_url) {
            resultsHTML += `
                <div class="breed-sprite">
                    <h4>Breed Sprite:</h4>
                    <pre class="text-sprite" id="text-sprite-container"></pre>
                </div>
            `;
            
            // Fetch and display text sprite
            fetch(`http://127.0.0.1:5000${data.sprite_url}`)
                .then(response => response.text())
                .then(spriteText => {
                    document.getElementById('text-sprite-container').textContent = spriteText;
                })
                .catch(error => {
                    console.error('Error loading sprite:', error);
                    document.getElementById('text-sprite-container').textContent = 'Error loading sprite';
                });
        }
        
        // Close the results card div
        resultsHTML += `</div>`;
        
        resultsContainer.innerHTML = resultsHTML;
    }
});