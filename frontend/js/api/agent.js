const BASE_URL = "http://127.0.0.1:8000"
export async function requestText(message) {
    const response = await fetch(`${BASE_URL}/api/v1/agent/text`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(message)
    });
    return await response.json();
}

export async function askPost(message, postId) {
    const response = await fetch(`${BASE_URL}/api/v1/agent/posts/${postId}/ask`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(message)
    });
    return await response.json();
}