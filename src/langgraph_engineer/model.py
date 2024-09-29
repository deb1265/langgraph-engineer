from langchain_openai import ChatOpenAI

def _get_model(config, default, key):
    model = config['configurable'].get(key, default)
    
    if model == "o1-mini":
        return ChatOpenAI(temperature=0, model_name="o1-mini")
    elif model == "o1-preview":
        return ChatOpenAI(temperature=0, model_name="o1-preview")
    elif model == "gpt-4o":
        return ChatOpenAI(temperature=0, model_name="gpt-4o")
    else:
        raise ValueError("Invalid model specified. Supported models: openai-oi-mini, openai-oi-preview, openai-gpt4o.")

