# Contributing

Oh, hello there! You're probably reading this because you are interested in
contributing to PyLadies. That's great to hear! This document will help you
through your journey of open source. Love it, cherish it, take it out to
dinner, but most importantly: read it thoroughly!

## What do I need to know to help

### Python basics

You'll need knowledge some knowledge of Python including what is a virtual
environment, pip for installing packages, and git basics. Feel free to ask in
PyLadies slack if you need suggestions for learning resources.

### Markdown and/or reStructuredText

While not a strict pre-requisite, familiarity with a markup language,
such as Markdown or reStructuredText, will help when editing the content pages
and files. We are working on moving all content files to Markdown which is
more commonly used and is more readable.

## What Python version do I need

We recommend using a recent version of Python such as 3.8 or higher. Please
use your operating system's package manager or a download from python.org.
Please avoid from using the system installed Python that came with your
operating system. The system Python is usually out of date, and it's a good
practice to leave the system Python unchanged for the operating system's use.

## How do I make a contribution

Never made an open source contribution before? Wondering how contributions work
in the PyLaides world? Here's a quick rundown!

1.  Find an issue that you are interested in addressing or a feature that you would like to address.
2.  Fork the repository associated with the issue to your GitHub account.
3.  Follow the installation instructions in the `README.md` file
4.  Create a new branch for your fix using:

```
$ git checkout -b branch-name-here
```

5. Make the appropriate changes for the issue you are trying to address or the feature that you want to add. Validate your changes by following the steps in the "How do I validate my changes" segment below.
6. Add and commit the changed files using `git add` and `git commit`.
7. Push the changes to the remote repository using:

```
$ git push origin branch-name-here
```

8. Submit a pull request to the upstream repository.
9. Title the pull request per the requirements outlined in the section below.
10. Set the description of the pull request with a brief description of what you did and any questions you might have about what you did.
11. Wait for the pull request to be reviewed by a maintainer.
12. Make changes to the pull request if the reviewing maintainer recommends them.
13. Celebrate your success after your pull request is merged! :tada:

## How should I write my commit messages and PR titles

Good commit messages serve at least three important purposes:

- To speed up the reviewing process.

- To help us write a good release note.

- To help the future maintainers of nteract/nteract (it could be you!), say
  five years into the future, to find out why a particular change was made to
  the code or why a specific feature was added.

Structure your commit message like this:

```
> Short (50 chars or less) summary of changes
>
> More detailed explanatory text, if necessary.  Wrap it to about 72
> characters or so.  In some contexts, the first line is treated as the
> subject of an email and the rest of the text as the body.  The blank
> line separating the summary from the body is critical (unless you omit
> the body entirely); tools like rebase can get confused if you run the
> two together.
>
> Further paragraphs come after blank lines.
>
>   - Bullet points are okay, too
>
>   - Typically a hyphen or asterisk is used for the bullet, preceded by a
>     single space, with blank lines in between, but conventions vary here
>
```

_Source: http://git-scm.com/book/ch5-2.html_

### DO

- Write the summary line and description of what you have done in the
  imperative mode, that is as if you were commanding. Start the line
  with "Fix", "Add", "Change" instead of "Fixed", "Added", "Changed".
- Always leave the second line blank.
- Line break the commit message (to make the commit message readable
  without having to scroll horizontally in gitk).

### DON'T

- Don't end the summary line with a period.

### Tips

- If it seems difficult to summarize what your commit does, it may be because it
  includes several logical changes or bug fixes, and are better split up into
  several commits using `git add -p`.

### References

The following blog post has a nice discussion of commit messages:

- "On commit messages" http://who-t.blogspot.com/2009/12/on-commit-messages.html

## How fast will my PR be merged

Your pull request will be merged as soon as there are maintainers to review it
and after tests have passed. You might have to make some changes before your
PR is merged but as long as you adhere to the steps above and try your best,
you should have no problem getting your PR merged.

That's it! You're good to go!

*Attribution: This document was inspired by the CONTRIBUTING.md file in the
[nteract/nteract](https://github.com/nteract/nteract/blob/master/CONTRIBUTING.md)
repo. Our thanks to [nteract](https://nteract.io) organization for this work.*