'''demonstrating common methods across sequences'''


example_sequence_list = [x for x in range(10)]
example_sequence_string = 'hello world'
example_sequence_range_object = range(10)

def start_string(method):
    return 'this is the {} of'.format(method)

#length
method = 'length'
print('{} lists {}'.format(start_string(method),len(example_sequence_list)))
print('{} string {}'.format(start_string(method),len(example_sequence_string)))
print('{} range object {}'.format(start_string(method),len(example_sequence_range_object)))

#max
method = 'max'
print('{} lists {}'.format(start_string(method),max(example_sequence_list)))
print('{} string {}'.format(start_string(method),max(example_sequence_string)))
print('{} range object {}'.format(start_string(method),max(example_sequence_range_object)))

#min
method = 'min'
print('{} lists {}'.format(start_string(method),min(example_sequence_list)))
print('{} string {}'.format(start_string(method),min(example_sequence_string)))
print('{} range object {}'.format(start_string(method),min(example_sequence_range_object)))

#sum
method = 'sum'
print('{} lists {}'.format(start_string(method),sum(example_sequence_list)))
print('{} string {}'.format(start_string(method),sum(example_sequence_string)))
print('{} range object {}'.format(start_string(method),sum(example_sequence_range_object)))

#all
method = 'all'
print('{} lists {}'.format(start_string(method),all(example_sequence_list)))
print('{} string {}'.format(start_string(method),all(example_sequence_string)))
print('{} range object {}'.format(start_string(method),all(example_sequence_range_object)))
#any