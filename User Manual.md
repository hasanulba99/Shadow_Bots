## How to Use ShadowBot Chatbot

### Chatting with ShadowBot
- Type any question or message into the input box and press **Enter**.
- ShadowBot will respond based on its AI model and conversation history.

### Uploading and Using CSV Files
- To upload a CSV file, type:  
  `upload csv`  
- Select your CSV file from the dialog box.
- Then ask for plots by typing commands like:  
  - `line plot Sales and Profit by Year`  
  - `bar plot Revenue by Region`  
  - `barh plot Quantity by Product`  

**CSV Plotting Instructions:**  
- The column name immediately after the word **“plot”** is used as the **x-axis**.  
- The column name after the word **“by”** is used as the **y-axis**.  
- You can plot multiple y-axis columns by listing them separated with **“and”**.  
- Example commands:  
  - `line plot Age by Salary`  
  - `bar plot Age and Experience by Salary`  

**Important:**  
Make sure to type the CSV column names **exactly as they appear** in your CSV (case-insensitive, but spelling and spaces must match).  
If column names are omitted or mistyped, the plot will not generate correctly.  
ShadowBot will generate the requested plots from your CSV data.

### Performing Web Searches
- To get real-time information, **include the word “search”** in your question, for example:  
  - `search about climate change`  
  - `search history of Python programming`  
- ShadowBot will perform a web search (via Wikipedia) and include relevant info in its response.

### Types of Answers ShadowBot Can Generate Offline
- General knowledge questions based on its pre-trained AI model.  
- Programming help, code snippets, and algorithm explanations.  
- Basic math, science, and language questions.  
- Conversation and contextual follow-ups based on previous inputs.  
- CSV data visualization and plotting commands.

### General Notes
- ShadowBot maintains conversation history for context.  
- You can combine chatting, data analysis, and searching naturally by using the appropriate keywords.
