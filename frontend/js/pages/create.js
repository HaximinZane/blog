import {CreatePost,ListTags} from "../api/client.js"

const form = document.getElementById("create_form");
const tags = document.getElementById("tags");
// tags是html的select元素，现在要渲染里面的选项
const old_tags = await ListTags()
tags.replaceChildren(...old_tags.map(tag => new Option(tag,tag)));




form.addEventListener("submit",async function(event){
    event.preventDefault();
    const title = document.getElementById("title").value;
    const summary = document.getElementById("summary").value;
    const content = document.getElementById("content").value;
    const status = document.getElementById("status").value;
    // tags 是html的select元素，获取选中的值
    const chosen_tags = Array.from(document.getElementById("tags").selectedOptions).map(option => option.value);
    const new_tags = document.getElementById("new_tags").value.split(",").map(tag => tag.trim()).filter(tag => tag.length > 0);
    const PostData = {
        author_id : 1,
        title : title,
        summary : summary,
        content : content,
        tags : chosen_tags.concat(new_tags),
        status : status
    }
    const post_id = await CreatePost(PostData);
    alert("创建成功");
    window.location.href = "post.html?id=" + post_id;
});
  