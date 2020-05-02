require 'csv'

measurements_file = 'cat_breeds_measurements.csv'
dataset_file = 'cats_dataset.csv'
samples_per_breed = 100..300

CSV.read(measurements_file, headers: true, converters: :float).flat_map do |cat|
  samples = rand(samples_per_breed)
  samples.times.map do
    [
      cat['Breed'],
      rand(cat['MinHeight']..cat['MaxHeight']).round(1),
      rand(cat['MinLength']..cat['MaxLength']).round(1),
      rand(cat['MinWeight']..cat['MaxWeight']).round(1)
    ]
  end
end.shuffle.yield_self do |cats|
  CSV.open(dataset_file, 'w') do |csv|
    csv << ['Breed', 'Height', 'Length', 'Weight']
    cats.each { |cat| csv << cat }
  end

  puts "#{cats.count} samples generated and written to #{dataset_file}"
end
