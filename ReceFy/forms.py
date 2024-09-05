from django import forms
from .models import Consejero, Dieta, Ingrediente, Receta, MiUsuario


#region Crud Ingredientes

class IngredienteForm(forms.ModelForm):
    receta = forms.ModelChoiceField(
        queryset=Receta.objects.all(),
        required=False,
        label="Receta",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Ingrediente
        fields = ['nombre', 'descripcion', 'cantidad', 'variedad', 'usos', 'p_nutricional', 'consejos', 
                  'grasas_saturadas', 'calorias', 'hidratos_de_carbono', 'grasas_trans', 
                  'total_carbohidratos', 'azucares', 'precio', 'receta']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'variedad': forms.TextInput(attrs={'class': 'form-control'}),
            'usos': forms.TextInput(attrs={'class': 'form-control'}),
            'p_nutricional': forms.TextInput(attrs={'class': 'form-control'}),
            'consejos': forms.TextInput(attrs={'class': 'form-control'}),
            'grasas_saturadas': forms.NumberInput(attrs={'class': 'form-control'}),
            'calorias': forms.NumberInput(attrs={'class': 'form-control'}),
            'hidratos_de_carbono': forms.NumberInput(attrs={'class': 'form-control'}),
            'grasas_trans': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_carbohidratos': forms.NumberInput(attrs={'class': 'form-control'}),
            'azucares': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['receta'].queryset = Receta.objects.all()
        self.fields['receta'].label_from_instance = lambda obj: f'{obj.id_receta} - {obj.nombre_plato}'

#endregion

#region CRUD Recetas

class RecetaForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(
        queryset=MiUsuario.objects.all(),
        required=False,
        label="Usuario",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    imagen = forms.ImageField(
        required=True,
        label="Imagen",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'})
    )

    class Meta:
        model = Receta
        fields = ['nombre_plato', 'imagen', 'categoria', 'temporada', 'origen', 'ingredientes', 'descripcion', 'instrucciones', 'tiempo_preparacion', 'dificultad', 'usuario']
        widgets = {
            'nombre_plato': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),
            'temporada': forms.TextInput(attrs={'class': 'form-control'}),
            'origen': forms.TextInput(attrs={'class': 'form-control'}),
            'ingredientes': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'instrucciones': forms.TextInput(attrs={'class': 'form-control'}),
            'tiempo_preparacion': forms.NumberInput(attrs={'class': 'form-control'}),
            'dificultad': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].queryset = MiUsuario.objects.all()
        self.fields['usuario'].label_from_instance = lambda obj: f'{obj.id} - {obj.first_name} - {obj.last_name}'

#endregion

#region Consejeros

class ConsejeroForm(forms.ModelForm):

    class Meta:
        model = Consejero
        fields = ['descripcion', 'titulacion', 'experiencia']
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'titulacion': forms.TextInput(attrs={'class': 'form-control'}),
            'experiencia': forms.TextInput(attrs={'class': 'form-control'}),
        }


#endregion

#region Dietas

class DietaForm(forms.ModelForm):
    usuario_id = forms.ModelChoiceField(
        queryset=MiUsuario.objects.all(),
        required=False,
        empty_label='Sistema Recetarium',
        label="Usuario",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    consejero_id = forms.ModelChoiceField(
        queryset=Consejero.objects.all(),
        required=False,
        empty_label='Sistema Recetarium',
        label="Consejero",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Dieta
        fields = ['nombre', 'descripcion', 'objetivo', 'calorias', 'condicion_medica',
                  'valor_nutricional', 'actividad_fisica', 'consejos', 'dispositivos',
                  'usuario_id', 'consejero_id', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'objetivo': forms.TextInput(attrs={'class': 'form-control'}),
            'calorias': forms.NumberInput(attrs={'class': 'form-control'}),
            'condicion_medica': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_nutricional': forms.NumberInput(attrs={'class': 'form-control'}),
            'actividad_fisica': forms.TextInput(attrs={'class': 'form-control'}),
            'consejos': forms.TextInput(attrs={'class': 'form-control'}),
            'dispositivos': forms.TextInput(attrs={'class': 'form-control'}),
            'usuario_id': forms.Select(attrs={'class': 'form-control'}),
            'consejero_id': forms.Select(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario_id'].queryset = MiUsuario.objects.all()
        self.fields['usuario_id'].label_from_instance = lambda obj: f'{obj.first_name} {obj.last_name}'
        self.fields['usuario_id'].empty_label = 'Sistema Recetarium'
        self.fields['consejero_id'].queryset = Consejero.objects.all()
        self.fields['consejero_id'].label_from_instance = lambda obj: f'{obj.nombre} {obj.apellido}'
        self.fields['consejero_id'].empty_label = 'Sistema Recetarium'


#endregion
