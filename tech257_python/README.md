# Python and Markdown

## Markdown basics

The `print()` function prints something to the screen: `print("Hello world!)`

```python
# Print message to the screen
print("Hello world!")
```

### Highlighting text

Wrap something in asterisks or underscores to get _italics_<br>
Wrap something in double asterisks to get **bold text**

### Lists

**Bullet points**

-   Hello
    -   Hello
    -   Hello
-   Hello

**Numbered List**

1. Hello
2. Hello
3. Hello

# Git

Git is a distributed version control system.

### Centralised vs Distributed VCS

-   A **Centralised VCS** stores all project files on a central server, with developers downloading files to work on them. This creates a single point of failure which increases the risk of data loss.
-   A **Distributed VCS** allows each developer to have a complete copy of the entire project, making it possible to work together simultaneously as well as reducing the risk of data loss.

![Centralised vs Distributed VCS](https://www.researchgate.net/profile/Sofia-Feist/publication/316553817/figure/fig2/AS:669480740982806@1536628055836/Centralized-Version-Control-vs-Distributed-Version-Control.ppm)

### Three Stages of Git

1. **Modified**: Changes made to files.
2. **Staged**: Files marked for inclusion in the next commit.
3. **Committed**: Data securely stored in your local repository.

### Common Workflow Commands

```
git init                 # Initialize a new Git repo
git add .                # Stage all modified files
git commit -m "message"  # Commit your changes
git push                 # Push changes to remote repo
git pull                 # Update local repo with remote changes
git log                  # View commit history
git diff <id> <id>       # View the difference between two commits
git checkout <id>        # SAFE revert locally to a previous commit to review files
git checkout <branch>    # Switch to a different branch
git reset --hard <id>    # DANGEROUS revert to previous commit id's state and destroy all changes since
git rm --cached          # Remove something from the git cache
```

### Branching

Branching in Git lets developers separate from the main line of development to continue to work independently without interfering with each other's changes.

Branching allows developers to work on new features or bug fixes in isolation from the main codebase.

Branching also allows developers to experiment with new ideas or approaches without the risk of affecting the main branch if something goes wrong.

## Difference Between Git and GitHub

While Git and GitHub are often mentioned together, they serve different roles in the development process. Git is a version control system that allows you to track changes, revert to previous stages, and collaborate on code. GitHub is a hosting service for Git repositories, providing a way to manage remote repositories. It has many features such as bug tracking, feature requests, task management, and continuous integration.

**Git** is a tool you install locally on your machine to manage your codebase, while **GitHub** is a service you use online to store your Git-managed projects and collaborate with others.

### Syncing Local and Remote Repositories

There are primarily two methods to sync your local repository with a remote repository:

1. **git push** : This command sends your committed changes to a remote repository. It's used to update the remote repository with the changes you've made locally.
2. **git pull** : This command fetches the changes from a remote repository and merges them into your local repository. It's used to keep your local repository up-to-date with the remote repository.

### Syncing Local Repo to Remote Repo

1. **Initialise a local Git repository**:

```
git init
```

2. **Add the remote repository**:

```
git remote add origin <url>
```

3. **Push your changes to the remote repository**:

```
git push -u origin main
```

```
Local Repo (Your machine)
       |
       | git push
       ↓
Remote Repo (GitHub)
       |
       | git pull
       ↓
Local Repo (Collaborator's machine)
```

### Removing a Folder/File from Remote Repository

1. **Delete the folder/file locally**:

```
git rm -r <folder-name>
git rm <file-name>
```

2. **Commit**:

```
git commit -m "Remove specific folder/file"
```

3. **Push the changes to the remote repository**:

```
git push
```

### Using a .gitignore File

The `.gitignore` file is used to tell Git which files or directories to ignore in a project. To use a `.gitignore` file:

1. create a `.gitignore` file in your project's root directory.
2. Add patterns for the files/directories to ignore:
    - For example, to ignore all `.txt` files, add `*.txt` to the `.gitignore` file.
    - To ignore a specific directory, add the path to the directory.
3. Commit:

```
git add .gitignore
git commit -m "Add .gitignore file"
```

### What is JSON and YAML?

## APIs

### What are API’s? How are they used and why are they so popular?

An API functions as a middleman enabling two separate applications to interact with each other. Whenever you check the weather on your phone or send a message to someone on WhatsApp, you are using an API. They set the rules for how data can be requested and received and are designed to be accessible to developers.

APIs are popular because they allow developers to access core functionality of another application quickly and easily. This saves time and resources and allows developers to focus on building the unique aspects of their application rather than reinventing everything themselves.

![](https://i.ibb.co/TvDnLm1/Blank-diagram.jpg)

### What is a REST API? What makes an API RESTful? What are the REST guidelines?

A REST API is an API that conforms to the constraints of REST architectural style and allows for interaction with RESTful web services.

An API is considered RESTful when it adheres to the following REST guidelines:

-   Requests managed through HTTP.
-   Stateless client-server communication, meaning no client information is stored between get requests and each request is separate and unconnected
-   Cacheable data that streamlines client-server interactions.
-   A uniform interface between components so that information is transferred in a standard form. This requires that:
    -   resources requested are identifiable and separate from the representations sent to the client.
    -   resources can be manipulated by the client via the representation they receive because the representation contains enough information to do so.
    -   self-descriptive messages returned to the client have enough information to describe how the client should process it.
    -   hypertext/hypermedia is available, meaning that after accessing a resource the client should be able to use hyperlinks to find all other
    -   currently available actions they can take.

### What is HTTP? (what does it stand for and what is it used for? What is HTTPS?)

**HTTP**: Hypertext Transfer Protocol is a protocol for fetching resources such as HTML documents. It is a client-server protocol meaning requests are initiated by the recipient, usually the web browser.

**HTTPS**: Hypertext Transfer Protocol Secure is the secure version of HTTP. HTTPS encrypts the data in transit to increase security and privacy. It is the primary protocol used to send data between a web browser and a website and is especially important when handling sensitive data such as login credentials and payment information.

### HTTP request structure

![](https://i.ibb.co/Z8P7Fjj/image.png)

**URL**: The address of the resource being requested.

**Request Verb**: Includes the method (GET, POST, etc.)

**Headers**: Key-value pairs providing information about the request.

**Body**: Optional data sent with POST and PUT requests.

### HTTP Response Structure

![](https://i.ibb.co/HFW5Cv1/image.png)

**Status Code**: A code that indicates whether the request was successful or not, e.g. 200, 404, etc.

**Status Message**: There could also be a message that provides more information, e.g. "OK", "Not Found", etc.

**Headers**: Key-value pairs providing information about the response.

**Body**: The data being sent back to the client, which could be the requested resource or error details.

### What are the 5 HTTP verbs and what do they do?

**GET** → Retrieves data from the server.

**POST** → Sends data to the server to be processed. Typically used to submit form data or upload a file in order to create new resources on the server.

**PUT** → Updates data on the server.

**PATCH** → Applies partial modifications to data on the server.

**DELETE** → Removes data from the server.

### Stateless vs Stateful

Stateless: Each request from client to server must contain all the information needed to understand and complete the request. There is no session information stored on the server.</br>Example: HTTP APIs where each request contains user authentication data.

Stateful: The server stores session information across requests.</br>Example: Traditional web applications where the server tracks user sessions.
