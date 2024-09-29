from langchain_openai import ChatOpenAI

def _get_model(config, default, key):
    model = config['configurable'].get(key, default)
    
    if model == "openai-oi-mini":
        return ChatOpenAI(temperature=0, model_name="oi-mini")
    elif model == "openai-oi-preview":
        return ChatOpenAI(temperature=0, model_name="oi-preview")
    elif model == "openai-gpt4o":
        return ChatOpenAI(temperature=0, model_name="gpt-4o")
    else:
        raise ValueError("Invalid model specified. Supported models: openai-oi-mini, openai-oi-preview, openai-gpt4o.")

