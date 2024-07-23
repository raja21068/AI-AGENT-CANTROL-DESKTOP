# AI Desktop Agent: Smart Automation & Task Management Platform

## Key Features
- **Compatibility**: Designed for various multimodal models.
- **Integration**: Currently integrated with **GPT-4o, Gemini Pro Vision, Claude 3 and LLaVa.**
-  **New Features**: Includes capabilities for downloading YouTube videos, copying text between files, and automating form filling and document uploads.
- **Future Plans**: Support for additional models.


## Modifying and Running Code
1. Make changes in `operate/main.py`
2. Run `pip install .` again
3. Run `operate` to see your changes


## Testing Changes
**After making significant changes, it's important to verify that SOC can still successfully perform a set of common test cases.**
In the root directory of the project, run:
```
python3 evaluate.py
```   
This will automatically prompt `operate` to perform several simple objectives.   
Upon completion of each objective, GPT-4v will give an evaluation and determine if the objective was successfully reached.   

`evaluate.py` will print out if each test case `[PASSED]` or `[FAILED]`. In addition, a justification will be given on why the pass/fail was given.   

It is recommended that a screenshot of the `evaluate.py` output is included in any PR which could impact the performance of SOC.



## Run `Self-Operating Computer`

1. **Install the project**
```
pip install AI-Desktop-Assistant-Agent-Based-Smart-Automation-Task-Management-Platform--chatgpt-4

```
2. **Run the project**
```
operate
```
3. **Enter your OpenAI Key**: If you don't have one, you can obtain an OpenAI key [here](https://platform.openai.com/account/api-keys)

4. **Give Terminal app the required permissions**: As a last step, the Terminal app will ask for permission for "Screen Recording" and "Accessibility" in the "Security & Privacy" page of Mac's "System Preferences".


## Using `operate` Modes

### Multimodal Models  `-m`
An additional model is now compatible with the Self Operating Computer Framework. Try Google's `gemini-pro-vision` by following the instructions below. 

Start `operate` with the Gemini model
```
operate -m gemini-pro-vision
```

**Enter your Google AI Studio API key when terminal prompts you for it** If you don't have one, you can obtain a key [here](https://makersuite.google.com/app/apikey) after setting up your Google AI Studio account. You may also need [authorize credentials for a desktop application](https://ai.google.dev/palm_docs/oauth_quickstart). It took me a bit of time to get it working, if anyone knows a simpler way, please make a PR.

#### Try Claude `-m claude-3`
Use Claude 3 with Vision to see how it stacks up to GPT-4-Vision at operating a computer. Navigate to the [Claude dashboard](https://console.anthropic.com/dashboard) to get an API key and run the command below to try it. 

```
operate -m claude-3
```



## OpenAI Rate Limiting Note
The ```gpt-4o``` model is required. To unlock access to this model, your account needs to spend at least \$5 in API credits. Pre-paying for these credits will unlock access if you haven't already spent the minimum \$5.   
Learn more **[here](https://platform.openai.com/docs/guides/rate-limits?context=tier-one)**
