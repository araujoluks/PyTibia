import tkinter as tk
from tkinter import messagebox, ttk
from src.repositories.radar.core import getCoordinate
from src.utils.core import getScreenshot
from .baseModal import BaseModal
from .refillModal import RefillModal
from .refillCheckerModal import RefillCheckerModal


class CavebotPage(tk.Frame):
    def __init__(self, parent, context):
        super().__init__(parent)
        self.context = context
        self.columnconfigure(0, weight=8)
        self.columnconfigure(1, weight=2)
        self.rowconfigure(1, weight=1)
        self.baseModal = None
        self.refillModal = None
        self.refillCheckerModal = None

        self.tableFrame = tk.LabelFrame(
            self, text='Waypoints', padx=10, pady=10)
        self.tableFrame.grid(column=0, row=0, rowspan=2, padx=10,
                             pady=10, sticky='nsew')
        self.tableFrame.rowconfigure(0, weight=1)
        self.tableFrame.columnconfigure(0, weight=1)

        self.table = ttk.Treeview(self.tableFrame, columns=(
            'label', 'type', 'coordinate', 'options'))
        self.table.grid(row=0, column=0, rowspan=1, sticky='nsew')
        self.table.bind('<Delete>', self.removeSelectedWaypoints)
        self.table.heading('label', text='Label')
        self.table.heading('type', text='Type')
        self.table.heading('coordinate', text='Coordinate')
        self.table.heading('options', text='Options')
        self.table.column('#0', width=0)
        self.table.column('label', width=100)
        self.table.column('type', width=100)
        self.table.column('coordinate', width=100)
        self.table.column('options', width=100)

        self.table.bind('<Double-1>', self.onWaypointDoubleClick)

        for waypoint in context.context['cavebot']['waypoints']['items']:
            self.table.insert('', 'end', values=(
                waypoint['label'], waypoint['type'], waypoint['coordinate'], waypoint['options']))

        self.waypointDirection = tk.StringVar(value='center')
        self.directionsFrame = tk.LabelFrame(
            self, text='Directions', padx=10, pady=10)
        self.directionsFrame.grid(column=1, row=0, padx=10,
                                  pady=10, sticky='nsew')
        self.directionsFrame.columnconfigure(0, weight=1)
        self.directionsFrame.columnconfigure(1, weight=1)
        self.directionsFrame.columnconfigure(2, weight=1)

        northOption = tk.Radiobutton(self.directionsFrame, variable=self.waypointDirection,
                                     text='North', value='north')
        northOption.grid(row=0, column=1)

        westOption = tk.Radiobutton(self.directionsFrame, variable=self.waypointDirection,
                                    text='West', value='west')
        westOption.grid(row=1, column=0)

        centerOption = tk.Radiobutton(self.directionsFrame, variable=self.waypointDirection,
                                      text='Center', value='center')
        centerOption.grid(row=1, column=1)

        eastOption = tk.Radiobutton(self.directionsFrame, variable=self.waypointDirection,
                                    text='East', value='east')
        eastOption.grid(row=1, column=2)

        southOption = tk.Radiobutton(self.directionsFrame, variable=self.waypointDirection,
                                     text='South', value='south')
        southOption.grid(row=2, column=1)

        self.actionsFrame = tk.LabelFrame(
            self, text='Actions', padx=10, pady=10)
        self.actionsFrame.grid(column=1, row=1, padx=10,
                               pady=10, sticky='nsew')
        self.actionsFrame.columnconfigure(0, weight=1, uniform='equal')
        self.actionsFrame.columnconfigure(1, weight=1, uniform='equal')

        self.walkButton = tk.Button(
            self.actionsFrame, text='Walk', command=lambda: self.addWaypoint('walk'))
        self.walkButton.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

        self.ropeButton = tk.Button(
            self.actionsFrame, text='Rope', command=lambda: self.addWaypoint('useRope'))
        self.ropeButton.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')

        self.shovelButton = tk.Button(
            self.actionsFrame, text='Shovel', command=lambda: self.addWaypoint('useShovel'))
        self.shovelButton.grid(row=1, column=1, padx=5, pady=5, sticky='nsew')

        self.moveUpButton = tk.Button(
            self.actionsFrame, text='Move Up', command=lambda: self.addWaypoint('moveUp'))
        self.moveUpButton.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')
        self.moveDownButton = tk.Button(
            self.actionsFrame, text='Move Down', command=lambda: self.addWaypoint('moveDown'))
        self.moveDownButton.grid(
            row=2, column=1, padx=5, pady=5, sticky='nsew')

        self.depositGoldButton = tk.Button(
            self.actionsFrame, text='Deposit gold', command=lambda: self.addWaypoint('depositGold'))
        self.depositGoldButton.grid(
            row=3, column=0, padx=5, pady=5, sticky='nsew')
        self.depositItemsButton = tk.Button(
            self.actionsFrame, text='Deposit items', command=lambda: self.addWaypoint('depositItems'))
        self.depositItemsButton.grid(
            row=3, column=1, padx=5, pady=5, sticky='nsew')

        self.dropFlasksButton = tk.Button(
            self.actionsFrame, text='Drop flasks', command=lambda: self.addWaypoint('dropFlasks'))
        self.dropFlasksButton.grid(
            row=4, column=0, padx=5, pady=5, sticky='nsew')

        self.refillButton = tk.Button(
            self.actionsFrame, text='Refill', command=lambda: self.openRefillModal())
        self.refillButton.grid(
            row=5, column=0, padx=5, pady=5, sticky='nsew')

        self.refillCheckerButton = tk.Button(
            self.actionsFrame, text='Refill checker', command=lambda: self.openRefillCheckerModal())
        self.refillCheckerButton.grid(
            row=5, column=1, padx=5, pady=5, sticky='nsew')

    def openBaseModal(self):
        if self.baseModal is None or not self.baseModal.winfo_exists():
            self.baseModal = BaseModal(self, onConfirm=lambda label, options: self.addWaypoint(
                'refill', options))

    def openRefillModal(self):
        if self.refillModal is None or not self.refillModal.winfo_exists():
            self.refillModal = RefillModal(self, onConfirm=lambda label, options: self.addWaypoint(
                'refill', options))

    def openRefillCheckerModal(self):
        if self.refillCheckerModal is None or not self.refillCheckerModal.winfo_exists():
            self.refillCheckerModal = RefillCheckerModal(self, onConfirm=lambda label, options: self.addWaypoint(
                'refillChecker', options))

    # TODO: verificar se a coordenada é walkable
    def addWaypoint(self, waypointType, options={}):
        screenshot = getScreenshot()
        coordinate = getCoordinate(screenshot)
        if coordinate is None:
            messagebox.showerror(
                'Erro', 'The Tibia minimap needs to be visible!')
            return
        waypointDirection = self.waypointDirection.get()
        if waypointDirection == 'north':
            coordinate = (coordinate[0], coordinate[1] - 1, coordinate[2])
        elif waypointDirection == 'south':
            coordinate = (coordinate[0], coordinate[1] + 1, coordinate[2])
        elif waypointDirection == 'east':
            coordinate = (coordinate[0] + 1, coordinate[1], coordinate[2])
        elif waypointDirection == 'west':
            coordinate = (coordinate[0] - 1, coordinate[1], coordinate[2])
        waypoint = {'label': '', 'type': waypointType,
                    'coordinate': coordinate, 'options': options}
        if waypointType == 'moveUp' or waypointType == 'moveDown':
            if waypointDirection == 'center':
                messagebox.showerror(
                    'Erro', 'Move Down or Move Up waypoint always needs a direction(North, West, East, South)')
                return
            waypoint['options']['direction'] = waypointDirection
        self.context.addWaypoint(waypoint)
        self.table.insert('', 'end', values=(
            waypoint['label'], waypoint['type'], waypoint['coordinate'], waypoint['options']))

    def removeSelectedWaypoints(self, _):
        selectedWaypoints = self.table.selection()
        for waypoint in selectedWaypoints:
            index = self.table.index(waypoint)
            self.table.delete(waypoint)
            self.context.removeWaypointByIndex(index)

    def onWaypointDoubleClick(self, event):
        item = self.table.identify_row(event.y)
        if item:
            index = self.table.index(item)
            waypoint = self.context.context['cavebot']['waypoints']['items'][index]
            if waypoint['type'] == 'refill':
                if self.refillModal is None or not self.refillModal.winfo_exists():
                    self.refillModal = RefillModal(
                        self, waypoint=waypoint, onConfirm=lambda label, options: self.updateWaypointByIndex(index, label=label, options=options))
            elif waypoint['type'] == 'refillChecker':
                if self.refillCheckerModal is None or not self.refillCheckerModal.winfo_exists():
                    self.refillCheckerModal = RefillCheckerModal(
                        self, waypoint=waypoint, onConfirm=lambda label, options: self.updateWaypointByIndex(index, label=label, options=options))
            else:
                if self.baseModal is None or not self.baseModal.winfo_exists():
                    self.baseModal = BaseModal(
                        self, waypoint=waypoint, onConfirm=lambda label, options: self.updateWaypointByIndex(index, label=label, options=options))

    def updateWaypointByIndex(self, index, label=None, options={}):
        self.context.updateWaypointByIndex(index, label=label, options=options)
        selecionado = self.table.focus()
        if selecionado:
            currentValues = self.table.item(selecionado)['values']
            if label is not None:
                currentValues[0] = label
            currentValues[3] = options
            self.table.item(selecionado, values=currentValues)
            self.table.update()
