## First of all, remember to do a proper:
git pull

## To make sure everything is up to date

## To create a new branch:
git checkout -b [new_branch_name]

## Push the branch to github:
git push origin [name_of_the_new_branch]

## Remember when you are commiting in a new branch
to make sure you are acctually in the right branch.

## When pushing your branch to remote, use:
git push --set-upstream origin [name_of_branch]

```bash
git checkout -b 'name'
# Do changes
git push --set-upstream origin addingMergeNotes
``

#Remember to commit and push the branch
'''
git commit -m 'comment' [file_names_changed]
git push --set-upstream origin [file_names]
'''
New fork added
