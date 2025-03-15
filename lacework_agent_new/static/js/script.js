// JavaScript for Lacework Agent Web Interface

document.addEventListener('DOMContentLoaded', function() {
    const questionForm = document.getElementById('questionForm');
    const submitBtn = document.getElementById('submitBtn');
    const loadingSpinner = document.getElementById('loadingSpinner');
    const answerOutput = document.getElementById('answerOutput');
    const modeSelect = document.getElementById('modeSelect');
    const questionInput = document.getElementById('questionInput');
    
    // Handle form submission
    questionForm.addEventListener('submit', async function(event) {
        event.preventDefault();
        
        // Get form data
        const mode = modeSelect.value;
        const question = questionInput.value.trim();
        
        // Validate input
        if (!question) {
            answerOutput.textContent = 'Please enter a question.';
            answerOutput.style.color = 'red';
            return;
        }
        
        // Show loading spinner
        submitBtn.disabled = true;
        loadingSpinner.classList.remove('d-none');
        answerOutput.textContent = 'Processing your question...';
        answerOutput.style.color = '';
        
        try {
            // Send request to API
            const response = await fetch('/api/ask', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    mode: mode,
                    question: question
                })
            });
            
            // Parse response
            const data = await response.json();
            
            // Display response
            if (response.ok) {
                answerOutput.textContent = data.response || 'No response received.';
            } else {
                answerOutput.textContent = `Error: ${data.error || 'Unknown error'}`;
                answerOutput.style.color = 'red';
            }
        } catch (error) {
            // Handle error
            console.error('Error:', error);
            answerOutput.textContent = `Error: ${error.message || 'Unknown error'}`;
            answerOutput.style.color = 'red';
        } finally {
            // Hide loading spinner
            submitBtn.disabled = false;
            loadingSpinner.classList.add('d-none');
        }
    });
    
    // Update placeholder based on selected mode
    modeSelect.addEventListener('change', function() {
        const mode = modeSelect.value;
        
        if (mode === 'prompt') {
            questionInput.placeholder = 'Enter your question here...';
        } else if (mode === 'agent') {
            questionInput.placeholder = 'Enter a complex task here (e.g., "Show me how to configure Lacework for AWS")...';
        } else if (mode === 'agentsdk') {
            questionInput.placeholder = 'Enter a complex task for the Agent SDK here...';
        }
    });
});
