import sublime, sublime_plugin
import Session
import socket
import sys

class DiffListener(sublime_plugin.EventListener):
    """Listens for modifications to the view and gets the diffs using 
    Operational Transformation"""

    def __init___(self):
        # watched_views is a sessions of which currently open views are bound to 
        # remote-collab sessions. This allows the  EventListener to check if
        # on_modified events happened to the views it cares about, or to other 
        # views which it doesn't care about.
        self.sessions = []

    def on_modified_async(self, view):
        """Listens for modifications to views which are part of a currently
        active remote session."""
        if sessions:
            for session in sessions if view in session.view:
                current_buffer = view.substr(sublime.Region(0, view.size())) 
                session.send_diffs(current_buffer)  

    def on_close(self, view): 
        """Check to see if views I care about are closed, and if they are,
        drop them from my watched-views"""
        if view in sessions.keys():
            del sessions[view]      

class StartSessionCommand(sublime_plugin.TextCommand):
    """Command to start a new RemoteCollab session for the current view"""
    get_buffer = lambda view: view.substr(sublime.Region(0, view.size()))

    def run(self):     
        # this will have to connect to the remote server (getting the address
        # from the settings file), wait for the server to generate the session,
        # and tell the user the access token. it'll then have to start watching
        # the urrent view synchronizing
        session = Session(self.view, is_true)
        DiffListener.sessions.append(session) = Session(session_id, get_buffer(self.view), is_true)
        session.patch
            
class ConnectToSessionCommand(sublime_plugin.ApplicationCommand):
    """Command to connect to an external RemoteCollab session."""
    # this will have to connect to the remote server (configured in settings file),
    # send the session token, make a new view containing the contents of the remote
    # session, and then start listening for modifications to that view and synchronizing
    
    def run(self):
        
        
