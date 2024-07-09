/**
 * Author: Shane Cooke
 * Date Created: 07/07/2024
 * Description: The chatbot class that enables users to interact with the chatbot, using it as a virtual assistant.
 *              The user can open/close the chatbox with a button, handled by toggleState().
 *              sendMessage() takes the user question, inserts the chat into the chat box, sends the question to the
 *              API for embedding and database search, which returns the appropriate answer. The answer is inserted
 *              into the chatbox.
 */



/**
 * Represents the chat box component.
 * @class
 */
class ChatBox {
    /**
     * Creates a new ChatBox instance.
     * @constructor
     */
    constructor() {
        this.args = {
            openButton: document.querySelector('.open-chatbox-button'),
            chatBoxDisplay: document.querySelector('.chatbox-display'),
            sendMessageButton: document.querySelector('.send-message'),
            chatBoxList: document.querySelector('.chatbox-body'),
            csrfToken: document.querySelector('[name=csrfmiddlewaretoken]').value
        };

        this.state = true;
        this.messages = [];
    }

    /**
     * Displays the chat box and sets up event listeners.
     */
    display() {
        const { openButton, chatBoxDisplay, sendMessageButton, chatBoxList } = this.args;

        openButton.addEventListener('click', () => this.toggleState(chatBoxDisplay));
        sendMessageButton.addEventListener('click', () => this.sendMessage(chatBoxDisplay));

        const node = chatBoxDisplay.querySelector('.chatbox-footer input');
        node.addEventListener('keyup', ({ key }) => {
            if (key === 'Enter') {
                this.sendMessage(chatBoxDisplay);
            }
        });
    }

    /**
     * Toggles the chat box state (open or closed). Adds/removes CSS style.
     * @param {Element} chatBoxDisplay - The chat box display container.
     */
    toggleState(chatBoxDisplay) {
        this.state = !this.state;
        console.log(this.state)

        if(this.state) {
            chatBoxDisplay.classList.add('visible')
        } else {
            chatBoxDisplay.classList.remove('visible')
        }
    }

    /**
     * Sends a user message to the API and displays the bot's reply.
     * The user message is extracted from the html input.
     * @param {Element} chatBoxDisplay - The chat box display container.
     */
    async sendMessage(chatBoxDisplay) {
        let userMessage = chatBoxDisplay.querySelector('.chatbox-footer input').value.trim();
        if (!userMessage) return;

        const chatLi = this.createChatLi(userMessage, 'user-messages');
        this.args.chatBoxList.appendChild(chatLi);

        chatBoxDisplay.querySelector('.chatbox-footer input').value = '';

        const botReply = await this.sendToApi(userMessage);
        const processedReply = this.processReply(botReply);
        const botChatLi = this.createChatLi(processedReply, 'bot-messages');
        this.args.chatBoxList.appendChild(botChatLi);
    }

    /**
     * Processes the bot's reply (replaces hyperlinks and line breaks).
     * @param {string} reply - The bot's reply.
     * @returns {string} Processed reply.
     */
    processReply(reply) {
        const hyperlinkMailtoPattern = /([\w.@]+)\s*\[HYPERLINK:\s*(mailto:[^\]]+)\]/g;
        const hyperlinkUrlPattern = /([\w]+)\s*\[HYPERLINK:\s*(https?:\/\/[^\]]+)\]/g;
    
        reply = reply.replace(hyperlinkMailtoPattern, (match, wordBefore, url) => {
            return `<a href="${url}">${wordBefore}</a>`;
        });

        reply = reply.replace(hyperlinkUrlPattern, (match, wordBefore, url) => {
            return `<a href="${url}">${wordBefore}</a>`;
        });

        reply = reply.replace(/\n/g, '<br>');

        return reply;
    }

    /**
     * Creates an HTML list item for a chat message.
     * @param {string} message - The chat message content.
     * @param {string} className - CSS class for styling ('user-messages', 'bot-messages').
     * @returns {Element} Created list item.
     */
    createChatLi(message, className) {
        const chatLi = document.createElement('li');
        chatLi.classList.add(className);
        let chatContent = `<p>${message}</p>`;
        chatLi.innerHTML = chatContent;

        return chatLi;
    }

    /**
     * Sends user input to the RestAPI which is connected to the backend and retrieves the bot's reply.
     * @param {string} userInput - User input message.
     * @returns {Promise<string>} Bot's reply.
     */
    async sendToApi(userInput) {
        try {
            const response = await fetch('/chatbot/api/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': this.args.csrfToken,
                },
                body: JSON.stringify({ user_input: userInput }),
            });

            if (response.ok) {
                const data = await response.json();
                return data.reply;
            } else {
                console.error('Error:', response.statusText);
                return "Sorry, something went wrong.";
            }
        } catch (error) {
            console.error('Error:', error);
            return "Sorry, something went wrong.";
        }
    }
}

const chatbox = new ChatBox();
chatbox.display();