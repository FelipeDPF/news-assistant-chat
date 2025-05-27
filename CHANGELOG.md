# Changelog

All notable changes to this project will be documented in this file.

### Overview
This is the first public beta release of the News Assistant project. It includes the full setup of the application frontend, designed to simulate a chat-based personal assistant for browsing daily or topic-specific news.  
**All features and changes listed below represent the complete work done since the initial project setup.**

## [0.1.0-beta] – 2025-05-27

### Added
- Created the initial structure of the news assistant chat interface.
- Integrated Bootstrap for styling and Font Awesome for icons.
- Added light and dark theme support with a toggle button.
- Implemented a chat container with responsive design and scrollable chat box.
- Styled user and assistant message bubbles to resemble social media chat interfaces.
- Added functionality to fetch news from NewsAPI.org based on user input.
- Displayed fetched news articles with titles, images, sources, authors, and links.
- Simulated typing effect for the assistant with a delay and `...` before displaying messages.
- Added a title ("📰 News Assistant") to the chat interface for better context.
- Implemented follow-up conversation flow where the assistant asks, "Looking for anything else?".
- Allowed the user to restart the conversation by saying "Hey".
- Added a friendly message when the user ends the conversation: "Got it! I'm here if you need more news later. 😊 Just say 'Hey' if you need anything!"

### Changed
- Adjusted chat container and chat box dimensions for a larger and more spacious interface.
- Enhanced message bubble styling with shadows and improved spacing.
- Updated assistant's dark theme message bubble color for better readability.

### Fixed
- Ensured smooth scrolling to the latest message in the chat box.
- Improved error handling for cases where no articles are found.

---

## [Unreleased]
### Planned/Upcoming

- Improve assistant responses to handle a wider range of inputs (e.g., greetings, confusion, thank you).
- Support follow-up questions or multi-step queries.
- Add loading indicator or typing animation while waiting for news results.
- Allow users to select news categories or country (e.g., Sports, Tech, US, CA).
- Add a "Clear Chat" button to restart the conversation manually.
- Make the chat UI fully responsive and resizable (especially for mobile).
- Use local storage or session to preserve conversation state.
- Write unit tests for the FastAPI backend.
- Add deployment instructions and config for platforms like Vercel or Render.