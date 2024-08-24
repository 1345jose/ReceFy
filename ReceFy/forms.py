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

