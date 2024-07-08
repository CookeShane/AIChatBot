class ChatBox {
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

    toggleState(chatBoxDisplay) {
        this.state = !this.state;
        console.log(this.state)

        if(this.state) {
            chatBoxDisplay.classList.add('visible')
        } else {
            chatBoxDisplay.classList.remove('visible')
        }
    }

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

    createChatLi(message, className) {
        const chatLi = document.createElement('li');
        chatLi.classList.add(className);
        let chatContent = `<p>${message}</p>`;
        chatLi.innerHTML = chatContent;

        return chatLi;
    }

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