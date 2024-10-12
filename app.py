from flask import Flask, render_template, request
import openai

app = Flask(__name__)

 
openai.api_key = "API KEY"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method == 'POST':
        name = request.form['name']
        height = request.form['height']
        weight = request.form['weight']
        age = request.form['age']
        preference = request.form['preference']
        cuisine = request.form['cuisine']
        
        prompt = (f"Create a balanced diet meal plan for {name}, aged {age}, with a height of {height} cm and weight of {weight} kg. Their dietary preference is {preference}, and they prefer {cuisine} cuisine. The meal plan should focus on healthy, nutrient-dense, and low-calorie options for weight management. Include five meals: breakfast, morning snack, lunch, afternoon snack, and dinner. For each meal, provide the dish and its nutritional breakdown (calories, carbs, proteins, fats), ensuring all meals are suitable for a diet-friendly regimen. Conclude with a total nutritional summary for the day, ensuring the plan supports a healthy weight loss or maintenance goal.")

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that generates detailed meal plans with nutritional information."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300
            )
            result = response['choices'][0]['message']['content'].strip()
        except Exception as e:
            result = f"An error occurred: {str(e)}"
        
        return render_template('result.html', result=result)

    return render_template('generate.html')

if __name__ == '__main__':
    app.run(debug=True)
