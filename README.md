# dim-wish-list-custom

Uses the voltron.txt file from dim-wish-list-sources by 48klocs (https://github.com/48klocs/dim-wish-list-sources).

To add your custom wish list:
    
    Select "Fork" on top right menu bar and "Create Fork".
    Go to "customList.txt" and paste your custom wish list.
   
To update wish list:

    Lists will automatically update once a day at midnight UTC
    
    If you want to update manually
      Navigate to ".github/workflows/update-wishlists.yml"
      Replace 
        schedule:
          - cron: "0 0 * * *"
      with
        push
      and commit changes.
      Under "Actions" there should be an action showing the update.
      Once finished, make sure to undo changes to ".github/workflows/update-wishlists.yml"

To add to DIM:

    Select a finalList.txt
    Go to raw version. Either click "view raw" link or button on top right side of text window.
    Copy URL of raw version
    On DIM, navigate to Settings-Wish Lists
    Paste under "Optionally, supply the URL(s) for a wish list (pipe | separated)"
    Click "Update Wish List Source"
