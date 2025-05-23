import requests

def call_api(method,url,data=None):
    try:
        if method == 'GET':
            response = requests.get(url)

        elif method == 'POST':
            response = requests.post(url,json=data)

        elif method == 'PUT':
            response = requests.put(url,json=data)

        elif method == 'DELETE':
            response = requests.delete(url)

        else:
            print("Invalid method")
            return None


        if 200 <= response.status_code < 300:
            return response.json()

        else:
            print("API Error: " , response.status_code)
            return None

    except Exception as e:
        print("Request failed: ", {e})
        return None



def get_all_post():
    url="https://jsonplaceholder.typicode.com/posts"
    posts = call_api('GET',url)

    if posts:
        for post in posts:
            print("\n-----------------------------")
            print(f"User ID: {post['userId']}")
            print(f"Post ID: {post['id']}")
            print(f"Title: {post['title']}")
            print(f"Body: {post['body']}")
    else:
        print("No posts found")

def get_post_by_id(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    post = call_api('GET', url)

    if post:
        print("\nPost Details")
        print("-------------------------------")
        print(f"User ID: {post['userId']}")
        print(f"Post ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print("-------------------------------")
        return post
    else:
        print("Post not found.")
        return None

def get_comments_by_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/comments?postId={post_id}"
    return call_api("GET", url)

def create_comment(post_id, name, email, body):
    comment_data = {
        "postId": post_id,
        "name": name,
        "email": email,
        "body": body
    }
    response = call_api("POST", "https://jsonplaceholder.typicode.com/comments", comment_data)

    if response is not None:
        print("Comment added successfully!")
        return response
    else:
        print("Failed to add comment.")
        return None

def update_post(post_id, new_title, new_body):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    updated_data = {
        "title": new_title,
        "body": new_body
    }
    response = call_api("PUT", url, updated_data)

    if response:
        print("Post updated successfully!")
        return response
    else:
        print("Failed to update post.")
        return None
def delete_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = call_api("DELETE", url)

    if response == {}:
        print("Post deleted successfully!")
        return True
    else:
        print("Failed to delete post.")
        return False

def main():
    print("Welcome! Fetching all posts...\n")
    get_all_post()

    while True:
        print("\nAvailable commands: SHOW, LIST, UPDATE, DELETE, QUIT")
        command = input("Enter a command: ").strip().lower()

        if command == "quit":
            print("Exiting program.")
            break

        elif command == "list":
            get_all_post()

        elif command == "show":
            try:
                post_id = int(input("Enter Post ID to show: "))
                post = get_post_by_id(post_id)

                if post:
                    comments = get_comments_by_post(post_id)
                    print("\nComments:")
                    for comment in comments:
                        print(f"- {comment['name']} ({comment['email']}): {comment['body']}")

                    while True:
                        next_action = input("Type 'add comment' or 'go back': ").strip().lower()
                        if next_action == "go back":
                            break
                        elif next_action == "add comment":
                            name = input("Your Name: ")
                            email = input("Your Email: ")
                            body = input("Your Comment: ")
                            create_comment(post_id, name, email, body)
                        else:
                            print("Invalid option.")
            except ValueError:
                print("Invalid post ID.")

        elif command == "update":
            try:
                post_id = int(input("Enter Post ID to update: "))
                title = input("New Title (press Enter to skip): ")
                body = input("New Body (press Enter to skip): ")
                update_post(post_id, title, body)
            except ValueError:
                print("Invalid post ID.")

        elif command == "delete":
            try:
                post_id = int(input("Enter Post ID to delete: "))
                confirm = input("Are you sure? (yes/no): ").strip().lower()
                if confirm == "yes":
                    delete_post(post_id)
                else:
                    print("Deletion cancelled.")
            except ValueError:
                print("Invalid post ID.")

        else:
            print("Invalid command. Please enter SHOW, LIST, UPDATE, DELETE, or QUIT.")

if __name__ == "__main__":
    main()