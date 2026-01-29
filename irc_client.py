#!/usr/bin/env python3
"""
Simple IRC Chat Client
A graphical IRC client with channel support and basic IRC features
"""

import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog
import re


class IRCClient:
    def __init__(self, master):
        self.master = master
        self.master.title("IRC Chat Client")
        self.master.geometry("800x600")
        
        self.socket = None
        self.connected = False
        self.nickname = ""
        self.current_channel = ""
        
        self.setup_ui()
        
    def setup_ui(self):
        # Top frame for connection controls
        top_frame = tk.Frame(self.master)
        top_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        
        tk.Label(top_frame, text="Server:").pack(side=tk.LEFT)
        self.server_entry = tk.Entry(top_frame, width=20)
        self.server_entry.insert(0, "irc.libera.chat")
        self.server_entry.pack(side=tk.LEFT, padx=5)
        
        tk.Label(top_frame, text="Port:").pack(side=tk.LEFT)
        self.port_entry = tk.Entry(top_frame, width=6)
        self.port_entry.insert(0, "6667")
        self.port_entry.pack(side=tk.LEFT, padx=5)
        
        tk.Label(top_frame, text="Nickname:").pack(side=tk.LEFT)
        self.nick_entry = tk.Entry(top_frame, width=15)
        self.nick_entry.pack(side=tk.LEFT, padx=5)
        
        self.connect_btn = tk.Button(top_frame, text="Connect", command=self.connect)
        self.connect_btn.pack(side=tk.LEFT, padx=5)
        
        self.disconnect_btn = tk.Button(top_frame, text="Disconnect", command=self.disconnect, state=tk.DISABLED)
        self.disconnect_btn.pack(side=tk.LEFT, padx=5)
        
        # Channel frame
        channel_frame = tk.Frame(self.master)
        channel_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        
        tk.Label(channel_frame, text="Channel:").pack(side=tk.LEFT)
        self.channel_entry = tk.Entry(channel_frame, width=20)
        self.channel_entry.pack(side=tk.LEFT, padx=5)
        
        self.join_btn = tk.Button(channel_frame, text="Join", command=self.join_channel, state=tk.DISABLED)
        self.join_btn.pack(side=tk.LEFT, padx=5)
        
        self.part_btn = tk.Button(channel_frame, text="Leave", command=self.part_channel, state=tk.DISABLED)
        self.part_btn.pack(side=tk.LEFT, padx=5)
        
        tk.Label(channel_frame, text="Current:").pack(side=tk.LEFT, padx=(20, 5))
        self.current_channel_label = tk.Label(channel_frame, text="None", fg="blue")
        self.current_channel_label.pack(side=tk.LEFT)
        
        # Chat display
        self.chat_display = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, state=tk.DISABLED)
        self.chat_display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Configure text tags for colors
        self.chat_display.tag_config("server", foreground="gray")
        self.chat_display.tag_config("error", foreground="red")
        self.chat_display.tag_config("info", foreground="green")
        self.chat_display.tag_config("user", foreground="blue")
        
        # Message input frame
        input_frame = tk.Frame(self.master)
        input_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)
        
        self.message_entry = tk.Entry(input_frame)
        self.message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.message_entry.bind("<Return>", lambda e: self.send_message())
        self.message_entry.config(state=tk.DISABLED)
        
        self.send_btn = tk.Button(input_frame, text="Send", command=self.send_message, state=tk.DISABLED)
        self.send_btn.pack(side=tk.LEFT)
        
    def display_message(self, message, tag=""):
        """Display a message in the chat window"""
        self.chat_display.config(state=tk.NORMAL)
        if tag:
            self.chat_display.insert(tk.END, message + "\n", tag)
        else:
            self.chat_display.insert(tk.END, message + "\n")
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)
        
    def connect(self):
        """Connect to IRC server"""
        server = self.server_entry.get().strip()
        port = self.port_entry.get().strip()
        nickname = self.nick_entry.get().strip()
        
        if not server or not port or not nickname:
            messagebox.showerror("Error", "Please fill in all connection fields")
            return
            
        try:
            port = int(port)
        except ValueError:
            messagebox.showerror("Error", "Port must be a number")
            return
            
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((server, port))
            
            self.nickname = nickname
            
            # Send IRC handshake
            self.socket.send(f"NICK {nickname}\r\n".encode('utf-8'))
            self.socket.send(f"USER {nickname} 0 * :{nickname}\r\n".encode('utf-8'))
            
            self.connected = True
            self.display_message(f"Connecting to {server}:{port} as {nickname}...", "info")
            
            # Start receive thread
            receive_thread = threading.Thread(target=self.receive_messages, daemon=True)
            receive_thread.start()
            
            # Update UI
            self.connect_btn.config(state=tk.DISABLED)
            self.disconnect_btn.config(state=tk.NORMAL)
            self.join_btn.config(state=tk.NORMAL)
            self.message_entry.config(state=tk.NORMAL)
            self.send_btn.config(state=tk.NORMAL)
            self.server_entry.config(state=tk.DISABLED)
            self.port_entry.config(state=tk.DISABLED)
            self.nick_entry.config(state=tk.DISABLED)
            
        except Exception as e:
            messagebox.showerror("Connection Error", f"Failed to connect: {str(e)}")
            self.connected = False
            if self.socket:
                self.socket.close()
                
    def disconnect(self):
        """Disconnect from IRC server"""
        if self.connected and self.socket:
            try:
                self.socket.send(b"QUIT :Goodbye!\r\n")
            except:
                pass
            self.socket.close()
            
        self.connected = False
        self.current_channel = ""
        self.display_message("Disconnected from server", "info")
        
        # Update UI
        self.connect_btn.config(state=tk.NORMAL)
        self.disconnect_btn.config(state=tk.DISABLED)
        self.join_btn.config(state=tk.DISABLED)
        self.part_btn.config(state=tk.DISABLED)
        self.message_entry.config(state=tk.DISABLED)
        self.send_btn.config(state=tk.DISABLED)
        self.server_entry.config(state=tk.NORMAL)
        self.port_entry.config(state=tk.NORMAL)
        self.nick_entry.config(state=tk.NORMAL)
        self.current_channel_label.config(text="None")
        
    def join_channel(self):
        """Join an IRC channel"""
        channel = self.channel_entry.get().strip()
        
        if not channel:
            messagebox.showerror("Error", "Please enter a channel name")
            return
            
        if not channel.startswith("#"):
            channel = "#" + channel
            
        if self.connected and self.socket:
            self.socket.send(f"JOIN {channel}\r\n".encode('utf-8'))
            self.current_channel = channel
            self.current_channel_label.config(text=channel)
            self.part_btn.config(state=tk.NORMAL)
            self.display_message(f"Joining {channel}...", "info")
            
    def part_channel(self):
        """Leave current channel"""
        if self.current_channel and self.connected and self.socket:
            self.socket.send(f"PART {self.current_channel}\r\n".encode('utf-8'))
            self.display_message(f"Left {self.current_channel}", "info")
            self.current_channel = ""
            self.current_channel_label.config(text="None")
            self.part_btn.config(state=tk.DISABLED)
            
    def send_message(self):
        """Send a message to the current channel"""
        message = self.message_entry.get().strip()
        
        if not message:
            return
            
        if not self.connected or not self.socket:
            messagebox.showerror("Error", "Not connected to server")
            return
            
        # Handle commands
        if message.startswith("/"):
            self.handle_command(message)
        else:
            # Send to current channel
            if self.current_channel:
                try:
                    self.socket.send(f"PRIVMSG {self.current_channel} :{message}\r\n".encode('utf-8'))
                    self.display_message(f"<{self.nickname}> {message}", "user")
                except Exception as e:
                    self.display_message(f"Error sending message: {str(e)}", "error")
            else:
                self.display_message("You must join a channel first", "error")
                
        self.message_entry.delete(0, tk.END)
        
    def handle_command(self, command):
        """Handle IRC commands"""
        parts = command.split(maxsplit=1)
        cmd = parts[0].lower()
        
        if cmd == "/join" and len(parts) > 1:
            channel = parts[1]
            if not channel.startswith("#"):
                channel = "#" + channel
            self.socket.send(f"JOIN {channel}\r\n".encode('utf-8'))
            self.current_channel = channel
            self.current_channel_label.config(text=channel)
            self.part_btn.config(state=tk.NORMAL)
            
        elif cmd == "/part" or cmd == "/leave":
            if self.current_channel:
                self.part_channel()
                
        elif cmd == "/msg" and len(parts) > 1:
            msg_parts = parts[1].split(maxsplit=1)
            if len(msg_parts) == 2:
                target, message = msg_parts
                self.socket.send(f"PRIVMSG {target} :{message}\r\n".encode('utf-8'))
                self.display_message(f"-> {target}: {message}", "user")
                
        elif cmd == "/nick" and len(parts) > 1:
            new_nick = parts[1]
            self.socket.send(f"NICK {new_nick}\r\n".encode('utf-8'))
            
        elif cmd == "/quit":
            self.disconnect()
            
        else:
            # Send raw command
            self.socket.send(f"{command[1:]}\r\n".encode('utf-8'))
            
    def receive_messages(self):
        """Receive and process messages from IRC server"""
        buffer = ""
        
        while self.connected:
            try:
                data = self.socket.recv(4096).decode('utf-8', errors='ignore')
                
                if not data:
                    break
                    
                buffer += data
                lines = buffer.split("\r\n")
                buffer = lines.pop()
                
                for line in lines:
                    if line:
                        self.process_message(line)
                        
            except Exception as e:
                if self.connected:
                    self.display_message(f"Connection error: {str(e)}", "error")
                break
                
        if self.connected:
            self.master.after(0, self.disconnect)
            
    def process_message(self, message):
        """Process incoming IRC messages"""
        # Handle PING
        if message.startswith("PING"):
            pong = message.replace("PING", "PONG")
            self.socket.send(f"{pong}\r\n".encode('utf-8'))
            return
            
        # Parse IRC message
        prefix = ""
        if message.startswith(":"):
            prefix, message = message[1:].split(" ", 1)
            
        parts = message.split(" ", 2)
        command = parts[0] if parts else ""
        
        # Handle different message types
        if command == "PRIVMSG":
            # Chat message
            if len(parts) >= 3:
                channel = parts[1]
                msg = parts[2]
                if msg.startswith(":"):
                    msg = msg[1:]
                    
                # Extract nickname from prefix
                nick = prefix.split("!")[0] if "!" in prefix else prefix
                
                self.display_message(f"<{nick}> {msg}")
                
        elif command == "JOIN":
            nick = prefix.split("!")[0] if "!" in prefix else prefix
            channel = parts[1].lstrip(":")
            self.display_message(f"* {nick} joined {channel}", "info")
            
        elif command == "PART":
            nick = prefix.split("!")[0] if "!" in prefix else prefix
            channel = parts[1]
            self.display_message(f"* {nick} left {channel}", "info")
            
        elif command == "QUIT":
            nick = prefix.split("!")[0] if "!" in prefix else prefix
            reason = parts[1].lstrip(":") if len(parts) > 1 else ""
            self.display_message(f"* {nick} quit ({reason})", "info")
            
        elif command == "NICK":
            old_nick = prefix.split("!")[0] if "!" in prefix else prefix
            new_nick = parts[1].lstrip(":")
            self.display_message(f"* {old_nick} is now known as {new_nick}", "info")
            if old_nick == self.nickname:
                self.nickname = new_nick
                
        elif command in ["001", "002", "003", "004", "005", "251", "252", "253", "254", "255", "265", "266", "372", "375", "376"]:
            # Server messages
            if len(parts) >= 2:
                msg = " ".join(parts[1:]).lstrip(":")
                self.display_message(msg, "server")
                
        elif command == "332":  # Topic
            if len(parts) >= 3:
                channel = parts[1]
                topic = parts[2].lstrip(":")
                self.display_message(f"Topic for {channel}: {topic}", "info")
                
        elif command == "353":  # Names list
            if len(parts) >= 3:
                names = parts[2].lstrip(":")
                self.display_message(f"Users: {names}", "info")
                
        elif command == "433":  # Nickname in use
            self.display_message("Nickname already in use!", "error")
            
        else:
            # Display other messages
            self.display_message(message, "server")


def main():
    root = tk.Tk()
    app = IRCClient(root)
    root.mainloop()


if __name__ == "__main__":
    main()
