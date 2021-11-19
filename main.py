# Crystals Generator
# Copyright © 2021 Mateusz Dera

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import bpy
import random
from math import radians

bl_info = {
    "name": "Crystals Generator",
    "description": "Plugin generates crystals.",
    "author": "Mateusz Dera",
    "version": (1, 0),
    "blender": (2, 93, 0),
    "tracker_url": "",
    "category": "Add Mesh"
}

class create(bpy.types.Operator):
    bl_idname = 'crystalsgenerator.create'
    bl_label = 'Generate crystal'

    def execute(self, context):
        #-=-=-=-=-=-=-=-=-
        x = bpy.context.scene.cursor.location.x
        y = bpy.context.scene.cursor.location.y
        z = bpy.context.scene.cursor.location.z

        vertices = context.scene.vertices
        height = context.scene.height
        top_height_in_percent = context.scene.top_height_in_percent

        bottom_width = context.scene.bottom_width
        middle_width = context.scene.middle_width
        top_width_in_percent = context.scene.top_width_in_percent

        rot_x_min = -15
        rot_x_max = 15

        rot_y_min = -15
        rot_y_max = 15

        rot_z_min = 0
        rot_z_max = 60

        #-=-=-=-=-=-=-=-
        top_height = height * (top_height_in_percent / 100)
        top_width =  middle_width * (top_width_in_percent / 100)

        #-=-=-=-=-=-=-=-
        bpy.ops.mesh.primitive_circle_add(vertices=vertices, radius=1, enter_editmode=True, align='WORLD', location=(x, y, z), scale=(1, 1, 1))
        bpy.ops.transform.resize(value=(bottom_width, bottom_width, bottom_width), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        bpy.ops.mesh.edge_face_add()
        bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, (height - top_height)), "orient_type":'NORMAL', "orient_matrix":((0.433884, 0.900969, -0), (-0.900969, 0.433884, 0), (0, 0, 1)), "orient_matrix_type":'NORMAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        bpy.ops.transform.resize(value=(middle_width, middle_width, middle_width), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        bpy.ops.transform.rotate(value=radians(random.randint(rot_x_min, rot_x_max)), orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        bpy.ops.transform.rotate(value=radians(random.randint(rot_y_min, rot_y_max)), orient_axis='Y', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        bpy.ops.transform.rotate(value=radians(random.randint(rot_z_min, rot_z_max)), orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, top_height), "orient_type":'NORMAL', "orient_matrix":((0.433884, 0.900969, -0), (-0.900969, 0.433884, 0), (0, 0, 1)), "orient_matrix_type":'NORMAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        if top_height_in_percent > 0:
            if top_width_in_percent <= 0:
                bpy.ops.mesh.merge(type='CENTER')
            else:
                bpy.ops.transform.resize(value=(top_width, top_width, top_width), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

        bpy.ops.object.editmode_toggle()
        return {"FINISHED"}

class main_panel(bpy.types.Panel):
    bl_idname = "panel.main_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Crystals"
    bl_category = "Crystals"

    def draw(self, context):
        layout = self.layout
        col1 = layout.column(align = True)
        col2 = layout.column(align = True)
        col3 = layout.column(align = True)
        col4 = layout.column(align = True)
        col5 = layout.column(align = True)
        col6 = layout.column(align = True)
        col7 = layout.column(align = True)
        col8 = layout.column(align = True)
        col9 = layout.column(align = True)
        col10 = layout.column(align = True)
        col11 = layout.column(align = True)
        col12 = layout.column(align = True)

        col1.prop(context.scene, "vertices")
        col2.prop(context.scene, "height")
        col3.prop(context.scene, "top_height_in_percent")
        col4.prop(context.scene, "bottom_width")
        col5.prop(context.scene, "middle_width")
        col6.prop(context.scene, "top_width_in_percent")
        
        col7.prop(context.scene, "rot_x_min")
        col8.prop(context.scene, "rot_x_max")

        col9.prop(context.scene, "rot_x_min")
        col10.prop(context.scene, "rot_x_max")

        col11.prop(context.scene, "rot_x_min")
        col12.prop(context.scene, "rot_x_max")

        layout.operator("crystalsgenerator.create", text="Generate crystal")

def register() :
    bpy.utils.register_class(create)
    bpy.utils.register_class(main_panel)
    bpy.types.Scene.vertices = bpy.props.IntProperty \
      (
        name = "Vertices",
        description = "Nuber of vertices",
        default = 7,
        min=3,
        step=1
      )
    bpy.types.Scene.height = bpy.props.FloatProperty \
      (
        name = "Height",
        description = "Crystal height",
        default = 10,
        min=1
      )
    bpy.types.Scene.top_height_in_percent = bpy.props.IntProperty \
      (
        name = "Top height",
        description = "Top height %",
        default = 20,
        min=0,
        max=100,
      )
    bpy.types.Scene.bottom_width = bpy.props.FloatProperty \
      (
        name = "Bottom",
        description = "Height of the middle",
        default = 1,
        min=1
      )
    bpy.types.Scene.middle_width = bpy.props.FloatProperty \
      (
        name = "Middle",
        description = "Height of the middle",
        default = 1.25,
        min=1,
      )
    bpy.types.Scene.top_width_in_percent = bpy.props.IntProperty \
      (
        name = "Top Width",
        description = "Top width %",
        default = 0,
        min=0,
        max=100,
      )
    
def unregister() :
    bpy.utils.unregister_class(create)
    bpy.utils.unregister_class(main_panel)
    del bpy.types.Scene.vertices
    del bpy.types.Scene.height
    del bpy.types.Scene.top_height_in_percent
    del bpy.types.Scene.bottom_width
    del bpy.types.Scene.middle_width
    del bpy.types.Scene.top_width_in_percent


if __name__ == "__main__" :
    register()
