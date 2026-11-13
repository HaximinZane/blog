const BASE_URL = "http://127.0.0.1:8000"
const API_PREFIX = "/api/v1"
export async function GetHealth(){
    try{
        const response = await fetch(BASE_URL+"/health");
        if(response.ok){
            return response.json();
        }
        else{
            throw new Error(`Error fetching health status: ${response.status}`);
        }
    }
    catch(error){
        throw error;
    }
}

const POST_PREFIX = BASE_URL+API_PREFIX+"/posts/"
export async function ListPosts(skip = 0,limit = 10){
    try{
        let list_prefix = `?skip=${skip}&limit=${limit}`;
        const response = await fetch(POST_PREFIX+list_prefix);
        if(!response.ok){
            throw new Error(`Error get Posts : ${response.status}`);
        }
        return response.json()
    }
    catch(error){
        throw error
    }
}

export async function GetPost(id){
    try{
        const response = await fetch(POST_PREFIX+`${id}`);   
        if (!response.ok) {
            throw new Error(`Error get Posts : ${response.status}`);
        }
        return response.json()
    }
    catch (error) {
        throw error
    }
}

export async function CreatePost(postData){
    try{
        const response = await fetch(POST_PREFIX,{
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(postData)
        });
        if(!response.ok){
            throw new Error(`Error create Post : ${response.status}`);
        }
        return response.json()
    }
    catch(error){
        throw error
    }
}

export async function ListTags(){
    try{
        const response = await fetch(BASE_URL+API_PREFIX+"/tags/");
        if(!response.ok){
            throw new Error(`Error get Tags : ${response.status}`);
        }
        return response.json()
    }
    catch(error){
        throw error
    }
}