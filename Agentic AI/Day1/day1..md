**There is not coding session for Day 1, just theory understanding**
## What is GenAI?
GenAI is simply an AI which can generate new content like text, audio, video, code, images etc. using patterns it learn from data<br>
It Gives probabilistic output based on user input.

## What is LLM?
LLM are GenAI model or Large Language model are simply neural networks trainded on billions of tokens or data.<br>
It predict the next the best possible token/word based previous one<br>
User enter prompt -> LLM tokenize prompt -> turns those tokens into numbers -> feed into transformers and get the result<br>
Predict model predict next possible token repeatedly to give output<br>
process continue until stop signal (like period or max tokens)

## What is Prompt?
Prompt is how we talk to LLM model <br>
In simple word it is programming language to interact with LLM models but instead of writing code we pass input in Natural Language<br>
Every good prompt must have these 4 stuff :- <br>
- Role : Give LLM a role like You are XYZ or Act as a XYZ
- Task : Task to complete
- Context : Provide context to LLM to get the best possible personalized response
- Input : Simply give input in prompt <br>
**Example : <role> You are a friendly expert tour guide. <br><task>Suggest a 5-day itinerary in Italy in June,<br> <Context> focused on food, art, and history.**<br>
Input is already embedded in it example prompt.<br>

Q : What is the role of temperature in LLM?<br>
A : temperature controls the randomness and creativity of LLM response. High temperature high randomness, low temperature - focused and more realistic output