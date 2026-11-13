from .client import client
from ..services.post_service import get_public_post

async def generate_text(message):
    agent = client()
    response = "推理过程:\n\n"

    reasoning,output,info = await agent.think(message)
    usage = info["usage"] 
    for text in reasoning:
        response += text

    response += "\n\n\n正文:\n\n"
    for text in output:
        response += text

    response += "\n\n\n元信息:\n"
    response += f"""
模型：{info["model"]}\n
响应状态：{info["status"]}\n
用量：\n
输入token: {usage.input_tokens}\n
输出token: {usage.output_tokens}  (推理: {usage.output_tokens_details.reasoning_tokens} token)\n
缓存命中:{usage.input_tokens_details.cached_tokens}\n 
"""
    await agent._client.close()
    return response

# async def generate_text_stream(message):
#     agent = client()
#     response = "推理过程:\n\n"

#     reasoning,output,info = await agent.think(message)
#     usage = info["usage"] 
#     for text in reasoning:
#         response += text
#         yield response

#     response += "\n\n\n正文:\n\n"
#     for text in output:
#         response += text
#         yield response

#     response += "\n\n\n元信息:\n"
#     response += f"""
# 模型：{info["model"]}\n
# 响应状态：{info["status"]}\n
# 用量：\n
# 输入token: {usage.input_tokens}\n
# 输出token: {usage.output_tokens}  (推理: {usage.output_tokens_details.reasoning_tokens} token)\n
# 缓存命中:{usage.input_tokens_details.cached_tokens}\n 
# """
#     yield response
    
async def llm_read_post(message:dict[str,str]):
    agent = client()

    reasoning,output,info = await agent.think(message)
    usage = info["usage"] 

    response = "\n\n\n正文:\n\n"
    for text in output:
        response += text

    response += "\n\n\n元信息:\n"
    response += f"""
模型：{info["model"]}\n
响应状态：{info["status"]}\n
用量：\n
输入token: {usage.input_tokens}\n
输出token: {usage.output_tokens}  (推理: {usage.output_tokens_details.reasoning_tokens} token)\n
缓存命中:{usage.input_tokens_details.cached_tokens}\n\n
---
"""
    await agent._client.close()
    return response   
