from langchain_community.embeddings.bedrock import BedrockEmbeddings

def get_embedding_function():
    embeddings = BedrockEmbeddings(
            credentials_profile_name="default", region_name="ap-southeast-2" # Use default Amazon credentials on ap-southeast-2 (Sydney) region.
            }
    return embeddings

