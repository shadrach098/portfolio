
        // Chat functionality
        let chatHistory = [];
        let isTyping = false;

        function toggleChat() {
            const chatWindow = document.getElementById('chatWindow');
            chatWindow.classList.toggle('open');
            
            if (chatWindow.classList.contains('open')) {
                document.getElementById('chatInput').focus();
            }
        }

        function handleKeyPress(event) {
            if (event.key === 'Enter' && !event.shiftKey) {
                event.preventDefault();
                sendMessage();
            }
        }

        async function sendMessage() {
            const input = document.getElementById('chatInput');
            const message = input.value.trim();
            
            if (!message || isTyping) return;
            
            // Add user message to history
            chatHistory.push({
                role: 'user',
                content: message,
                timestamp: new Date().toISOString()
            });
            
            // Add user message to UI
            addMessage(message, 'user');
            input.value = '';
            
            // Show typing indicator
            showTypingIndicator();
            
            // Send to your API with chat history
            try {
                const response = await callChatbotAPI(message, chatHistory);
                removeTypingIndicator();
                
                // Add bot response to history
                chatHistory.push({
                    role: 'assistant',
                    content: response,
                    timestamp: new Date().toISOString()
                });
                
                addMessage(response, 'bot');
            } catch (error) {
                removeTypingIndicator();
                addMessage('Sorry, I encountered an error. Please try again.', 'bot');
            }
        }

        function addMessage(text, sender) {
            const messagesContainer = document.getElementById('chatMessages');
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${sender}-message`;
            messageDiv.innerHTML = `<p>${text}</p>`;
            messagesContainer.appendChild(messageDiv);
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }

        function showTypingIndicator() {
            isTyping = true;
            const messagesContainer = document.getElementById('chatMessages');
            const typingDiv = document.createElement('div');
            typingDiv.className = 'typing-indicator';
            typingDiv.id = 'typingIndicator';
            typingDiv.innerHTML = '<span></span><span></span><span></span>';
            messagesContainer.appendChild(typingDiv);
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }

        function removeTypingIndicator() {
            isTyping = false;
            const typingIndicator = document.getElementById('typingIndicator');
            if (typingIndicator) {
                typingIndicator.remove();
            }
        }

        // API Integration
        // Replace the callChatbotAPI function with this updated version:
        async function callChatbotAPI(message, history) {
            const contextWindow = 10;
            const recentHistory = history.slice(-contextWindow);
            
            try {
                const response = await fetch('https://cool-gannet-annually.ngrok-free.app/api/chat/Agent', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                        'Authorization': 'thread_KRCTwvVOh9QbwALTaC2TWhvN'  // Added 'Bearer' prefix
                    },
                    body: JSON.stringify({
                        message: message,
                        memory: recentHistory,
                        Thread: 'thread_KRCTwvVOh9QbwALTaC2TWhvN'
                    })
                });
                
                if (!response.ok) {
                    console.error('API Response:', response.status, response.statusText);
                    throw new Error(`API request failed: ${response.status}`);
                }
                
                const data = await response.json();
                return data.response || data.message || data.text;
            } catch (error) {
                console.error('API Error:', error);
                throw error;
            }
        }
